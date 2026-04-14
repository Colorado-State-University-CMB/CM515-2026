// ==== SELECT INPUT FILE ====
inputPath = File.openDialog("Select a .czi file");

// Extract directory and filename (no extension)
dir = File.getParent(inputPath);
name = File.getNameWithoutExtension(inputPath);

// Define output path automatically
outputPath = dir + File.separator + name;

// ==== OPEN FILE ====
open(inputPath);
title = getTitle();

// ==== SPLIT CHANNELS ====
run("Split Channels");

// Generate channel names dynamically
c1 = "C1-" + title;
c2 = "C2-" + title;
c3 = "C3-" + title;
c4 = "C4-" + title;

// SET DISPLAY RANGES 
selectWindow(c3);
setMinAndMax(4, 75);

selectWindow(c1);
setMinAndMax(1, 300);

// MERGE CHANNELS 
run("Merge Channels...", "c1=" + c1 + " c3=" + c3 + " create");

//  Z PROJECTION 
run("Z Project...", "projection=[Max Intensity]");

// CONVERT TO RGB 
run("Stack to RGB");

// ADD SCALE BAR 
run("Scale Bar...", "width=10 height=10 thickness=10 font=20 location=[Lower Left] bold overlay");

// SAVE 
saveAs("PNG", outputPath + "-Pretty_RGB.png");