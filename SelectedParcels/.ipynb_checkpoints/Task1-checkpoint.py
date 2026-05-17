
#import arcpy module
import arcpy
#Connct to created lab7 geodatabase
arcpy.env.workspace = r"C:\Users\ealmousa\Downloads\lab7_data\lab7.gdb"
arcpy.env.overwriteOutput = True #set overwrite permission if new file exists


#Set fc_powerline to Powerline
fc_powerline='Powerline'
#Set fc_parcel to Parcels
fc_parcel='Parcels'

#MakeFeatureLayer_management creates a feature layer from an input feature class or layer file.
#The layer that is created by the tool is temporary and will not persist after the session ends unless the layer is saved to disk or the map document is saved
arcpy.MakeFeatureLayer_management(fc_powerline,"powerline_lyr")
arcpy.MakeFeatureLayer_management(fc_parcel,"parcel_lyr")

#Set buffer_output to powerline buffer
buffer_output='powerline_buffer'

#Buffer Analysis Creates buffer around input features to a specified distance, in this case 250 feet.
arcpy.Buffer_analysis('powerline_lyr',buffer_output,"250 Feet")

#Select feature by location syntax:
#Syntax: SelectLayerByLocation_management (in_layer, {overlap_type}, {select_features}, {search_distance}, {selection_type})
#Selects features in a layer based on a spatial relationship to features in another layer.
arcpy.SelectLayerByLocation_management("parcel_lyr","WITHIN","powerline_buffer")



# create output feature class 
sr = arcpy.Describe("parcel_lyr").spatialReference
#http://pro.arcgis.com/en/pro-app/tool-reference/data-management/create-feature-class.htm
#Creates an empty feature class in a geodatabase or a shapefile in a folder.
arcpy.CreateFeatureclass_management(out_path=arcpy.env.workspace,out_name="selected_parcels",geometry_type="Polygon",template=fc_parcel,has_m="SAME_AS_TEMPLATE",has_z="SAME_AS_TEMPLATE",spatial_reference=sr)
#add selection to output feature class
arcpy.Append_management("parcel_lyr","selected_parcels")




