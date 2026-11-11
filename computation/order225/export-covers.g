# Exhaustively classify SmallGroup(225,i), i=1..NrSmallGroups(225),
# and export every subgroup of order 15 for every one of the six groups.
LoadPackage("SmallGrp");
n := 15;
N := 225;
# Run GAP from this directory so the output files land beside the script.
coverfile := "covers-15.jsonl";
classfile := "classification-225.tsv";
PrintTo(coverfile, "");
PrintTo(classfile, "id\texp\tabelian\tnilpotent\tnorm3\tnorm5\tH15\tstructure\n");
total := NrSmallGroups(N);
Print("GAP ", GAPInfo.Version, "; order=", N, "; groups=", total, "\n");
for i in [1..total] do
  G := SmallGroup(N, i);
  exp := Exponent(G);
  P := SylowSubgroup(G, 3);
  Q := SylowSubgroup(G, 5);
  elts := AsList(G);
  identity_index := Position(elts, Identity(G)) - 1;
  classes := ConjugacyClassesSubgroups(G);
  subs := DuplicateFreeList(Filtered(Concatenation(List(classes, Elements)), h -> Size(h) = n));
  AppendTo(coverfile, "{\"id\":", i, ",\"exp\":", exp,
           ",\"identity_index\":", identity_index, ",\"subs\":[");
  first := true;
  for h in subs do
    if not first then AppendTo(coverfile, ","); fi;
    first := false;
    helts := AsList(h);
    AppendTo(coverfile, "[");
    for j in [1..Size(helts)] do
      if j > 1 then AppendTo(coverfile, ","); fi;
      AppendTo(coverfile, Position(elts, helts[j]) - 1);
    od;
    AppendTo(coverfile, "]");
  od;
  AppendTo(coverfile, "]}\n");
  AppendTo(classfile, i, "\t", exp, "\t", IsAbelian(G), "\t", IsNilpotent(G),
           "\t", IsNormal(G, P), "\t", IsNormal(G, Q), "\t", Length(subs),
           "\t", StructureDescription(G), "\n");
  Print("done ", N, " ", i, " exp ", exp, " subs ", Length(subs),
        " structure ", StructureDescription(G), "\n");
od;
Print("finished all ", total, " groups of order ", N, "\n");
QUIT;
