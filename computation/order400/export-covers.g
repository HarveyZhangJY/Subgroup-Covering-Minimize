# C2 / n = 20: export all subgroups of order 20 of every SmallGroup(400, i).
#
# Run from the workspace root:
#   PATH="/c/gap-4.10.2/bin/i686-pc-cygwin-default32-kv3:$PATH" \
#     "C:/gap-4.10.2/gap.exe" -l /proc/cygdrive/C/gap-4.10.2 -q -A computation/order400/export-covers.g
#
# One JSON record per group that passes the exponent test 20 mod Exponent(G) = 0
# (a necessary condition: if G is covered by subgroups of order 20, every
# element order divides 20, hence Exponent(G) | 20).  Groups failing the test
# are logged as "skip" and cannot be covered at all.
#
# Element labels are 0-based positions in AsList(G).  Extra metadata
# (structure description, Sylow normality, element orders) is saved so that
# audit.py can run fully offline.
#
# Optional batching: if batch-20.g exists in this directory it is Read instead
# of the default full range [1..NumberSmallGroups(400)]; that file must call
# ExportCovers itself (used only if some group turns out to be extremely slow).

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

if IsExistingFile("C:/Users/Felix/Documents/deepseek-harness/group-split2/computation/order400/batch-20.g") then
  Read("C:/Users/Felix/Documents/deepseek-harness/group-split2/computation/order400/batch-20.g");
else
  ExportCovers(20, 400, [1..NumberSmallGroups(400)],
    "C:/Users/Felix/Documents/deepseek-harness/group-split2/computation/order400/covers-20.jsonl", 2, 5);
fi;
QUIT;
