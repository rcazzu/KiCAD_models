(Kicad 9.0)

This is a quick guide on how to import parts:
There are 3 types of file:

.kycad_sym:  schematic symbol in Kicad. Declares pins.
.kycad_mod:  footprints. Those must be attached to its correct schematic symbol.
.step:       3d model. 


When you download KiCAD, by default you will have 2 important routes. 

*The 'internal' route,
which brings a lot of components models and footprints by default, and its often located on

C:\Program Files\KiCad\(version)\share\kicad

The important folders are 'symbols', 'footprints', and '3dmodels'.

*The 'secondary' route is 

C:\Users\(User)\....\Documents\KiCad\(version)

As long as you configure your rutes correctly in Kicad (preferences -> configure routes)
you will not encounter problem. You may use any of those routes for updating: 
I personally prefer adding new templates and resources on the secondary route, but updating 
the main one can have is advantages too.

Either way, the procedure is simple and the same for both. 
You have to download these files and adding them into their respective folders
There is one extra add for footprints: they must be in a folder with ending
'.pretty', inside of footprints folder

