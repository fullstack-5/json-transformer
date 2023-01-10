# Scenario -  JSON Transformation

## Please check the instructions to start the application from here [TestMe.md](https://github.com/fullstack-5/json-transformer/blob/main/TestMe.md)


## Problem Statement

Create an application that will do below

## Code Generator
+ Accept a source JSON structure
+ Accept a target JSON structure
+ Accept a mapping (provided in a CSV format)
+ Build an app that will generate the code required to transform the source JSON structure to target JSON structure based on the mapping[***Key Feature***]
+ The generated code should preferably be Python or NodeJS.
+ If you are using any transformation libraries like JQ/JSONATA/JOLT to achieve the mapping and transformation, the application should auto generate the spec files needed for these libraries [***Key Feature***]
+ Application should be generic enough to accept different source/target/mapping inputs and dynamically arrive at the required code to do the conversion.

## Code Executor 

+ Maintain a list of mapping-specification or generated-code specification by name. 
+ Expose an REST API endpoint which will accept source_json and specification name as input. 
+ REST API should accept the source_json, apply the transformation dynamically based on the generated code and respond back with transformed json. 
+ Based on the inputs received, automatically pick up the generated code and execute the same. 
+ Output should be the intended transformed JSON. 
+ Even if the generated code is executed with different data of same JSON structure, the intended output should be achieved.


## Other Guidelines

### Input Data
+ Refer to the below path in repo for sample data
       
       - data
        |- sample_1
        |- sample_2
        |- sample_3
        
