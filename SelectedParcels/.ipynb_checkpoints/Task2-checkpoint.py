
#import arcpy and os modules
import arcpy
import os

#locate path file with lab7_data
arcpy.env.workspace = r"C:\Users\ealmousa\Downloads\lab7_data"

arcpy.CheckOutExtension("Spatial") #Once the Spatial Analyst extension license has been retrieved by the script, tools using that extension can be used. 

#Individual bands within a multi-band file are known in ArcPy as Band_1, Band_2, etc.
#Appending the name of a band to the file name retrieves the corresponding band.

#Prints cell size in y, cell size in x, number of rows, number of columns
desc = arcpy.Describe("Elevation.tif/Band_1")
print("cell size in y direction", desc.meanCellHeight) 
print("cell size in x direction", desc.meanCellWidth)
print("#number of rows", desc.height)         
print("#number of colums", desc.width)         


#### create a RGB color-shaded Choropleth map using a DEM raster
inraster = arcpy.Raster('elevation.tif')  
desc = arcpy.Describe(inraster)


#converts to slope path by switching inraster to slope form
#Slope function Identifies the slope (gradient or steepness) from each cell of a raster.
inraster = arcpy.sa.Slope(inraster)

#get min and max
arcpy.CalculateStatistics_management(inraster)
MINResult = arcpy.GetRasterProperties_management(inraster, "MINIMUM")
zMin = float(MINResult.getOutput(0))
MAXResult = arcpy.GetRasterProperties_management(inraster, "MAXIMUM")
zMax = float(MAXResult.getOutput(0))
print(zMin, zMax)

#assign rows to height and cols to width
rows = desc.height
cols = desc.width

#assign outNae variable to a new file called Elevation_Colored_Slope_Final.tif
outName = 'Elevation_Colored_Slope_Final.tif'

#check if file already exists and remove it if it does
if os.path.exists(outName):
     os.remove(outName)

#create raster of scaled elevations using scale factor calculation
f = ((inraster -zMin)/(zMax-zMin))
#create the red raster 
R = 255* (inraster/inraster)
#green and blue raster values are identical
G = f * 255
B = f * 255

#http://pro.arcgis.com/en/pro-app/tool-reference/data-management/composite-bands.htm
#Compose single band datasets to a TIFF format raster file
arcpy.CompositeBands_management(str(R)+';'+str(G)+';'+str(B),outName)

#Print following statement when finshed
print("New RGB composite color-shaded image generated.")
