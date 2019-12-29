from pyswip import Prolog
prolog = Prolog()

#rules

prolog.assertz("is3DLimited(X) :- hasXMin(X), hasXMax(X), hasYMin(X), hasYMax(Y), hasZMin(X), hasZMax(X)")
prolog.assertz("hasPosition(X) :- hasX(X), hasY(X), hasZ(X)")
prolog.assertz("zone(X) :- spatial3D(X)")
prolog.assertz("site(X) :- zone(X), hasBuilding(X)")
prolog.assertz("building(X) :- zone(X), hasUsage(X)")
prolog.assertz("storey(X) :- zone(X), isLevel(X)")
prolog.assertz("space(X) :- zone(X), is3DLimited(X)")
prolog.assertz("element(X) :- hasTechnicalFunction(X)")
prolog.assertz("element(X) :- hasForm(X)")
prolog.assertz("element(X) :- hasPosition(X)")
