---
author: "Terri Wilson"
status: "Published"
document version: "Is this different to the software version?"
type: "update-note"
title: "Viewing supplier booking with load mode of Loose Cargo and its related records in Order Explorer"
product: "CargoWise"
module: "Core / Documents"
summary: Should this be included in the header?
language: "English"
search terms: ""
release_date: "2025-08-20"
reissue date: "Make a change"
published date: "2025-10-02"
duration: ""
course series: "Product learning"
membership level: "Software User"
software version: "v25.8.20.116"
---
##### **Update Note**

# Update the log message in DED Service Task

## Core / Documents

##### 20 August 2025  

##### (Specific Country)

***

### Summary

The DED Service Task, which handles deletion of eDocs from external storage has been enhanced to provide more accurate log messages.

***

### Description

some text

Previously, when the DED Service Task completed without deleting any files, the log message misleadingly stated:<br>
‘Run Completed, successfully deleted 0 eDocs from external storage.’

If one or more files are deleted, the message stated:<br>
‘Run Completed, successfully deleted {number of files} eDocs from external storage.’

These messages will now be replaced with the below message:

If one or more files are deleted:<br>
‘Run started.<br>
{number of} eDocs successfully processed for deletion.<br>
Run completed.’

If there are no files to be deleted:<br>
‘Run started.<br>
No eDocs to process for deletion.<br>
Run completed.’

All other log messages (e.g., errors, warnings) remain unaffected.

> [!ACTION]
**Support** Press the F1 key from anywhere within CargoWise to raise an eRequest.
>
> 1. Available in CargoWise 25.8.20.116 and later releases.
> 2. CargoWise Reference: 20250820e / WI00913271
