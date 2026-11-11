ExportCovers := function(n, ids, outfile)
  local N, i, G, elts, classes, subs, h, j, first;
  N := n^2;
  for i in ids do
    G := SmallGroup(N, i);
    if n mod Exponent(G) = 0 then
      elts := AsList(G);
      classes := ConjugacyClassesSubgroups(G);
      subs := Filtered(Concatenation(List(classes, Elements)), h -> Size(h) = n);
      AppendTo(outfile, "{\"id\":", i, ",\"exp\":", Exponent(G), ",\"subs\":[");
      first := true;
      for h in subs do
        if not first then AppendTo(outfile, ","); fi;
        first := false;
        AppendTo(outfile, "[");
        for j in [1..Size(h)] do
          if j > 1 then AppendTo(outfile, ","); fi;
          AppendTo(outfile, Position(elts, AsList(h)[j]) - 1);
        od;
        AppendTo(outfile, "]");
      od;
      AppendTo(outfile, "]}\n");
      Print("done ", N, " ", i, " subs ", Size(subs), "\n");
    else
      Print("skip ", N, " ", i, " exp ", Exponent(G), "\n");
    fi;
  od;
end;
# Run GAP from this directory (or pass an explicit output path).
ExportCovers(12, [1..NumberSmallGroups(144)], "covers-12.jsonl");
QUIT;
