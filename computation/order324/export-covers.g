# Export all subgroups of order 18 for the 176 groups of order 324 = 18^2.
# Element indices are 0-based positions in AsList(G).
# Each output line is one JSON object:
#   {"id":i,"exp":e,"subs":[[e0,...,e17],...]}
# Usage (defaults export all 176 groups into covers-18.jsonl):
#   PATH="..." gap.exe -l /proc/cygdrive/C/gap-4.10.2 -q -A computation/order324/export-covers.g
# Optional batching via environment variables PQALPHA_LO / PQALPHA_HI / PQALPHA_OUT.
# A group whose exponent does not divide 18 cannot be covered by subgroups of
# order 18 at all (every element of such a subgroup has order dividing 18);
# those groups are logged as "skip ... exp ..." and not exported.

ExportCoversRange := function(lo, hi, outfile)
  local i, G, exp, elts, classes, subs, h, parts, str, t;
  for i in [lo..hi] do
    t := Runtime();
    G := SmallGroup(324, i);
    exp := Exponent(G);
    if 18 mod exp <> 0 then
      Print("skip 324 ", i, " exp ", exp, "\n");
    else
      elts := AsList(G);
      classes := ConjugacyClassesSubgroups(G);
      subs := Filtered(Concatenation(List(classes, Elements)), h -> Size(h) = 18);
      parts := List(subs, h -> Concatenation("[",
        JoinStringsWithSeparator(
          List(AsList(h), x -> String(Position(elts, x) - 1)), ","), "]"));
      str := Concatenation("{\"id\":", String(i), ",\"exp\":", String(exp),
        ",\"subs\":[", JoinStringsWithSeparator(parts, ","), "]}\n");
      AppendTo(outfile, str);
      Print("done 324 ", i, " subs ", Length(subs), " ms ", Runtime() - t, "\n");
    fi;
  od;
end;

GetOpt := function(name, default)
  if IsBound(GAPInfo.SystemEnvironment) and
     IsBound(GAPInfo.SystemEnvironment.(name)) then
    return GAPInfo.SystemEnvironment.(name);
  fi;
  return default;
end;

lo := Int(GetOpt("PQALPHA_LO", "1"));
hi := Int(GetOpt("PQALPHA_HI", "176"));
out := GetOpt("PQALPHA_OUT",
  "C:/Users/Felix/Documents/deepseek-harness/group-split2/computation/order324/covers-18.jsonl");

Print("# export range ", lo, "..", hi, " of 1..", NumberSmallGroups(324),
      " into ", out, "\n");
ExportCoversRange(lo, hi, out);
Print("# export range finished\n");
QUIT;
