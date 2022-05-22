
module roundedCube(xdim ,ydim ,zdim, rdim){
	hull(){ // https://youtu.be/gKOkJWiTgAY
		translate([rdim, rdim, 0]) cylinder(zdim, rdim, rdim);
		translate([xdim-rdim, rdim, 0]) cylinder(zdim, rdim, rdim);
		translate([rdim, ydim-rdim, 0]) cylinder(zdim, rdim, rdim);
		translate([xdim-rdim, ydim-rdim, 0]) cylinder(zdim, rdim, rdim);
	}
}

module Trinket_shield(){
    /*
    // Pi lower left 
    translate([0, 0, 0])
        color("pink")
        difference(){
            cylinder(standoffThickness, standoffDia / 2, standoffDia / 2);
            translate([0, 0, -4])
            cylinder(standoffThickness * 2, standoffHoleDia / 2, standoffHoleDia / 2);
        }
    */

    // Pi upper left 
    translate([0, 17.8, 0])
        color("pink")
        difference(){
            cylinder(standoffThickness, standoffDia / 2, standoffDia / 2);
            cylinder(standoffThickness, standoffHoleDia / 2, standoffHoleDia / 2);
        }

    // Pi upper right 
    translate([50.8, 17.8, 0])
        color("pink")
        difference(){
            cylinder(standoffThickness, standoffDia / 2, standoffDia / 2);
            cylinder(standoffThickness, standoffHoleDia / 2, standoffHoleDia / 2);
        }

    // Pi lower right 
    translate([50.8, 0, 0])
        color("pink")
        difference(){
            cylinder(standoffThickness, standoffDia / 2, standoffDia / 2);
            cylinder(standoffThickness, standoffHoleDia / 2, standoffHoleDia / 2);
        }
}

module Arduino(){

    // Arduino lower left (power jack)
    translate([14, 2.5, 0])
        color("lightblue")
        difference(){
            cylinder(standoffThickness, standoffDia / 2, standoffDia / 2);
            cylinder(standoffThickness, standoffHoleDia / 2, standoffHoleDia / 2);
        }

    // upper left (USB)
    translate([14 + 1.3, (53.3 - 2.5), 0])
        color("lightblue")
        difference(){
            cylinder(standoffThickness, standoffDia / 2, standoffDia / 2);
            cylinder(standoffThickness, standoffHoleDia / 2, standoffHoleDia / 2);
        }

    // upper right
    translate([14 + 50.8, (53.3 - 2.5 - 15.2), 0])
        color("lightblue")
        difference(){
            cylinder(standoffThickness, standoffDia / 2, standoffDia / 2);
            cylinder(standoffThickness, standoffHoleDia / 2, standoffHoleDia / 2);
        }

    // lower right
    translate([14 + 50.8, (53.3 - 2.5 - 15.2 - 27.9), 0])
        color("lightblue")
        difference(){
            cylinder(standoffThickness, standoffDia / 2, standoffDia / 2);
            cylinder(standoffThickness, standoffHoleDia / 2, standoffHoleDia / 2);
        }
}
