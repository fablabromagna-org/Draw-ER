$fn = 64;

include <FLRModule.scad>


baseThickness = 2.4;
cornerRounding = 8;
plateOffset = 0;    // shift entire plate on x axis
railOffset = 16;     // plate lenght - railLength
M3holeDia = 3.5;
M3nutDia = 6.5;
holeOffset = M3holeDia * 1.2;
batteryOffset = 15;
casterFromEdge = 4;   // from edge to CL of caster bolt holes
cassis_wid = 75; // 94 for full Raspberry Pi, 84 for A+ ?
cassis_len = 140;


penDiameter = 15.0;
penRadius = penDiameter / 2;
baseLen = 34.5;
baseWid = 20;

railWidth = 2;

cutout_len = 45;
cutout_wid = 15;

trinketX = -41.5;
trinketY = -50.8/2;
sensor_offset = 13;



difference(){
    
    union(){
        // cassis plate
        translate([-cassis_len / 2 - plateOffset, -cassis_wid / 2, 0])
        roundedCube(cassis_len, cassis_wid, baseThickness, cornerRounding);
        

        // rails
        rail_offset = 5.5;
        translate([-cassis_len / 2 - plateOffset, 
                   +rail_offset+railWidth, baseThickness / 2])
            rotate([90, 0, 0])    
            roundedCube(cassis_len/2-8, 3.0, railWidth, 1);

        translate([-cassis_len / 2 - plateOffset, 
                   - rail_offset, baseThickness / 2])
            rotate([90, 0, 0])    
            roundedCube(cassis_len/2-8, 3.0, railWidth, 1); 

        translate([8, 
                   - rail_offset+railWidth -2, baseThickness / 2])
            rotate([90, 0, 0])    
            roundedCube(cassis_len/2-8, 3.0, railWidth, 1);

        translate([8, 
                   + rail_offset +2, baseThickness / 2])
            rotate([90, 0, 0])    
            roundedCube(cassis_len/2-8, 3.0, railWidth, 1); 


        
        //battery standoffs
        translate([batteryOffset, 0, baseThickness - 1])
        cylinder(baseThickness, standoffDia + 1, standoffDia + 1);  
        translate([batteryOffset + 15, 0, baseThickness - 1])
        cylinder(baseThickness, standoffDia + 1, standoffDia + 1);
        //translate([batteryOffset + 30, 0, baseThickness - 1])
        //cylinder(baseThickness, d=standoffDia + 1, d=standoffDia + 1);   

        //translate([-batteryOffset, 0, baseThickness - 1])
        //cylinder(baseThickness, d=standoffDia + 1, d=standoffDia + 1);  
        translate([-batteryOffset - 0, 0, baseThickness - 1])
        cylinder(baseThickness, standoffDia + 1, standoffDia + 1);
        translate([-batteryOffset - 15, 0, baseThickness - 1])
        cylinder(baseThickness, standoffDia + 1, standoffDia + 1);        

        // caster standoffs
        translate([cassis_len / 2 - casterFromEdge - plateOffset, -15, baseThickness -1])
        cylinder(baseThickness, standoffDia + 1, standoffDia + 1);  
        translate([cassis_len / 2 - casterFromEdge - plateOffset, 15, baseThickness -1])
        cylinder(baseThickness, standoffDia + 1, standoffDia + 1); 

        // trinket standoffs
        translate([trinketX, trinketY, 0])
        cylinder(standoffThickness, standoffDia / 2, standoffDia / 2);
        
        translate([trinketX + 17.8, trinketY, 0])
        cylinder(standoffThickness, standoffDia / 2, standoffDia / 2);        

        translate([trinketX + 17.8, trinketY + 50.8, 0])
        cylinder(standoffThickness, standoffDia / 2, standoffDia / 2);

        translate([trinketX, trinketY + 50.8, 0])
        cylinder(standoffThickness, standoffDia / 2, standoffDia / 2);        

        // nose standoffs
        translate([cassis_len/2 - 14, trinketY, 0])
        cylinder(standoffThickness, standoffDia / 2, standoffDia / 2);

        translate([cassis_len/2 - 14, trinketY + 50.8, 0])
        cylinder(standoffThickness, standoffDia / 2, standoffDia / 2); 

        
    }

    // center pen hole
    cylinder(baseThickness * 2, penRadius, penRadius);

   
    // caster holes
    translate([cassis_len / 2 - casterFromEdge - plateOffset, -15, 0])
    cylinder(baseThickness*2, M3holeDia, M3holeDia);     
    translate([cassis_len / 2 - casterFromEdge - plateOffset, 15, 0])
    cylinder(baseThickness*2, M3holeDia, M3holeDia);    

    // caster nut nolders
    translate([cassis_len / 2 - casterFromEdge - plateOffset, -15, baseThickness - 1])
    cylinder(baseThickness, M3nutDia, M3nutDia, $fn=6);
    translate([cassis_len / 2 - casterFromEdge - plateOffset, 15, baseThickness - 1])
    cylinder(baseThickness, M3nutDia, M3nutDia, $fn=6);

 
    // battery holes
    translate([batteryOffset, 0, 0])
    cylinder(baseThickness, M3holeDia, M3holeDia);  
    translate([batteryOffset + 15, 0, 0])
    cylinder(baseThickness, M3holeDia, M3holeDia);
    
    translate([-batteryOffset - 0, 0, 0])
    cylinder(baseThickness, M3holeDia, M3holeDia);
    translate([-batteryOffset - 15, 0, 0])
    cylinder(baseThickness, M3holeDia, M3holeDia); 

    // battery nut nolders
    translate([batteryOffset, 0, baseThickness - 1])
    cylinder(baseThickness, M3nutDia, M3nutDia, $fn=6);
    translate([batteryOffset + 15, 0, baseThickness - 1])
    cylinder(baseThickness, M3nutDia, M3nutDia, $fn=6);

    translate([-batteryOffset - 0, 0, baseThickness - 1])
    cylinder(baseThickness, M3nutDia, M3nutDia, $fn=6);
    translate([-batteryOffset - 15, 0, baseThickness - 1])
    cylinder(baseThickness, M3nutDia, M3nutDia, $fn=6);

    // trinket holes
    translate([trinketX, trinketY, 0])
    cylinder(standoffThickness * 2, standoffHoleDia / 2, standoffHoleDia / 2);

    translate([trinketX + 17.8, trinketY, 0])
    cylinder(standoffThickness * 2, standoffHoleDia / 2, standoffHoleDia / 2);

    translate([trinketX, trinketY + 50.8, 0])
    cylinder(standoffThickness * 2, standoffHoleDia / 2, standoffHoleDia / 2);

    translate([trinketX + 17.8, trinketY + 50.8, 0])
    cylinder(standoffThickness * 2, standoffHoleDia / 2, standoffHoleDia / 2);

    // nose standoff holees
    translate([cassis_len/2-14, trinketY, 0])
    cylinder(standoffThickness * 2, standoffHoleDia / 2, standoffHoleDia / 2);

    translate([cassis_len/2 -14, trinketY + 50.8, 0])
    cylinder(standoffThickness * 2, standoffHoleDia / 2, standoffHoleDia / 2);

 
}


standoffDia = 7;
standoffThickness = 5.5;
standoffHoleDia = 2;
