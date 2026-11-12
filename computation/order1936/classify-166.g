LoadPackage("SmallGrp");
G := SmallGroup(1936,166);
Cen := Center(G);
Print("center ", Size(Cen), " ", StructureDescription(Cen), "\n");
proj := NaturalHomomorphismByNormalSubgroup(G, Cen);
cls := ConjugacyClassesSubgroups(G);
subs := Filtered(Concatenation(List(cls, Elements)), h -> Size(h) = 44);
Print("total order44 subgroups ", Length(subs), "\n");
counts := [];
for H in subs do
  K := Intersection(H, Cen);
  im := Image(proj, H);
  key := [Size(im), Size(K)];
  p := Position(counts, key);
  if p = fail then Add(counts, key); Add(counts, 1); else counts[p+1] := counts[p+1] + 1; fi;
od;
Print("counts [image order, kernel size] = ", counts, "\n");
QUIT;
