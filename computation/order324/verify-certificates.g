# Independent GAP verification of the saved 27-subgroup certificates for
# SmallGroup(324,121) and SmallGroup(324,170).
#
# The script parses the saved JSONL data itself:
#   covers-18.jsonl      -> all subgroups of order 18 for those two ids
#   solutions-18.jsonl   -> the selected subgroup indices of the 27-covers
# For each selected element set S it checks, inside GAP, that S generates a
# subgroup of order 18 = |S| (i.e. S is closed), that S occurs among the
# subgroups enumerated by ConjugacyClassesSubgroups, and that the union of
# the 27 sets is all 324 elements. Nothing here uses the MILP.

ParseJsonInt := function(tok)
  return Int(Filtered(tok, c -> c in "0123456789"));
end;

# return the record (id, subs) of one covers-18.jsonl line
ParseCoversLine := function(line)
  local t, p;
  t := SplitString(line, "\"");
  p := Position(t, "subs");
  return rec(id := ParseJsonInt(t[3]),
             subs := EvalString(t[p + 1]{[2 .. Length(t[p + 1]) - 1]}));
end;

# return the record (id, selected) of one solutions-18.jsonl line
ParseSolutionsLine := function(line)
  local t, p;
  t := SplitString(line, "\"");
  p := Position(t, "selected");
  if p = fail then return fail; fi;
  return rec(id := ParseJsonInt(t[3]),
             selected := EvalString(t[p + 1]{[2 .. Length(t[p + 1]) - 1]}));
end;

dir := "C:/Users/Felix/Documents/deepseek-harness/group-split2/computation/order324/";
targets := [121, 170];

solutions := rec();
for line in SplitString(StringFile(Concatenation(dir, "solutions-18.jsonl")), "\n") do
  if Length(line) > 0 then
    r := ParseSolutionsLine(line);
    if r <> fail and r.id in targets then solutions.(String(r.id)) := r; fi;
  fi;
od;

for line in SplitString(StringFile(Concatenation(dir, "covers-18.jsonl")), "\n") do
  if Length(line) > 0 then
    c := ParseCoversLine(line);
    if c.id in targets then
      G := SmallGroup(324, c.id);
      elts := AsList(G);
      sol := solutions.(String(c.id));
      sel := sol.selected;
      if Length(sel) <> 27 or Length(Set(sel)) <> 27 then
        Error("selected list is not 27 distinct indices");
      fi;
      # every enumerated subgroup, as a sorted element-index tuple
      enumerated := Set(List(c.subs, s -> Set(s)));
      union := [];
      allsub := true;
      for j in sel do
        S := Set(c.subs[j + 1]);
        if Length(S) <> 18 then Error("saved set does not have size 18"); fi;
        H := Subgroup(G, List(S, x -> elts[x + 1]));
        if Size(H) <> 18 then
          Print("BAD ", c.id, " index ", j, " generates order ", Size(H), "\n");
          allsub := false;
        fi;
        if not (S in enumerated) then
          Print("BAD ", c.id, " index ", j, " not in enumerated subgroup list\n");
          allsub := false;
        fi;
        union := Union(union, S);
      od;
      Print("CERT ", c.id, " subgroups=27 all_saved_sets_are_order18_subgroups=",
            allsub, " pairs=", 27 * 18, " union=", Length(union),
            " covers_all=", Length(union) = 324, "\n");
      Print("CERT ", c.id, " structure=", StructureDescription(G),
            " exponent=", Exponent(G),
            " sylow2_normal=", IsNormal(G, SylowSubgroup(G, 2)),
            " sylow3_normal=", IsNormal(G, SylowSubgroup(G, 3)), "\n");
      Print("CERT ", c.id, " union_generates_order=",
            Size(Subgroup(G, List(union, x -> elts[x + 1]))), "\n");
      if not allsub or Length(union) <> 324 then
        Error("certificate verification failed");
      fi;
    fi;
  fi;
od;
Print("# certificate verification finished\n");
QUIT;
