# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2023-10-18 22:48:50
"""
import arcpy

def Model():  # Model

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False


    # Process: Select (Select) (analysis)
    Output_Feature_Class = ""
    arcpy.analysis.Select(in_features="", out_feature_class=Output_Feature_Class)

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace="C:\\Users\\Administrator\\Documents\\ArcGIS\\Projects\\Wildfire_Mangement\\Wildfire_Mangement.gdb", workspace="C:\\Users\\Administrator\\Documents\\ArcGIS\\Projects\\Wildfire_Mangement\\Wildfire_Mangement.gdb"):
        Model()
