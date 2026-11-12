# n = 44 = 11 * 2^2: export all subgroups of order 44 of SmallGroup(1936,i).
# Run from this directory: gap -q -A export-covers.g
# One JSON record per group with 44 mod Exponent(G) = 0; element labels are
# 0-based positions in AsList(G). Extra metadata supports offline auditing.
# Optional batching: if batch-44.g exists it is Read instead of the full range.

ListString := function(l)
  local s, i;
  s := "[";
  for i in [1..Length(l)] do
    if i > 1 then Append(s, ","); fi;
    Append(s, String(l[i]));
  od;
  Append(s, "]");
  return s;
end;

ExportCovers := function(n, N, ids, outfile, p, q)
  local out, i, G, e, elts, classes, subs, h, hl, first, line;
  out := OutputTextFile(outfile, true);
  SetPrintFormattingStatus(out, false);
  for i in ids do
    G := SmallGroup(N, i);
    e := Exponent(G);
    if n mod e = 0 then
      elts := AsList(G);
      classes := ConjugacyClassesSubgroups(G);
      subs := Filtered(Concatenation(List(classes, Elements)), x -> Size(x) = n);
      line := Concatenation(
        "{\"id\":", String(i),
        ",\"exp\":", String(e),
        ",\"structure\":\"", StructureDescription(G), "\"",
        ",\"p\":", String(p), ",\"q\":", String(q),
        ",\"sylow_p_normal\":", String(IsNormal(G, SylowSubgroup(G, p))),
        ",\"sylow_q_normal\":", String(IsNormal(G, SylowSubgroup(G, q))),
        ",\"orders\":", ListString(List(elts, Order)),
        ",\"subs\":[");
      first := true;
      for h in subs do
        if not first then Append(line, ","); fi;
        first := false;
        hl := AsList(h);
        Append(line, ListString(List(hl, x -> Position(elts, x) - 1)));
      od;
      Append(line, "]}");
      PrintTo(out, line, "\n");
      Print("done ", N, " ", i, " subs ", Size(subs), "\n");
    else
      Print("skip ", N, " ", i, " exp ", e, "\n");
    fi;
  od;
  CloseStream(out);
end;

if IsExistingFile("batch-44.g") then
  Read("batch-44.g");
else
  GetOpt := function(name, default)
    if IsBound(GAPInfo.SystemEnvironment) and
       IsBound(GAPInfo.SystemEnvironment.(name)) then
      return GAPInfo.SystemEnvironment.(name);
    fi;
    return default;
  end;
  lo := Int(GetOpt("LO", "1"));
  hi := Int(GetOpt("HI", String(NumberSmallGroups(1936))));
  out := GetOpt("OUT", "covers-44.jsonl");
  ExportCovers(44, 1936, [lo..hi], out, 11, 2);
fi;
QUIT;
