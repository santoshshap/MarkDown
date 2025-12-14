---
###########################################################################################################
# This is the official update note template, all future templates should be based on this as a reference. #
###########################################################################################################

# Required front matter in YAML, completed by Publishing Review Team
published: true                     # Reviewer use only, determines if the UPN should be published or not. False if not.
title: Document Title               # Not to be confused with the filename, this will be used specifically for the label on the link.
product: CargoWise
search_terms: ['20250723e','some','search', 'terms'] # Example reference / tracking code (alphanumeric treated as plain string)
summary: |                          # Multiline summary allowed; preserves paragraph breaks
  Summary text from UPN.

  This can span multiple lines without needing explicit quotes.

  Keep content concise—avoid Markdown headings or lists inside summary.
access_warning: false               # true = show access warning, false = hide
release_date: 2025-11-12            # ISO YYYY-MM-DD (safe unquoted)
reissue_date: ""                    # Blank = not reissued yet
published_date: 2025-11-12          # Initial publish date
duration: 7                         # Minutes (numeric only). Default 7. Duration it will take to read content.
course_series: Product learning     
membership_level: Software User      

version_numbers:                    # Nested object containing all tracked release identifiers as strings
  software_version: "25.8.31.544"
  dpr: "25.8.29.167"
  std: "25.8.27.373"
  gp1: "25.8.10.537"
  gp2: "25.8.10.511"

collect_feedback: true              # Boolean, true or false

# Permissions
editing_division: ""                # Blank -> default all divisions
editing_department: ""              # Blank -> default all departments
study_access: ""                    # Blank -> default private
study_division: ""                  # Blank -> all divisions
study_department: ""                # Blank -> all departments
---

# Update Note template with Test Data

## Product / Module

##### 01 September 2025  

##### (Reissue 01 January 2026)

***

### Summary <!-- In UPN MD Heading 3 is used for section headings -->

This template demonstrates all acceptable Markdown syntax, formatting styles, and UI elements for Update Notes (UPNs). Use this as a reference guide to understand supported features including headings, lists, tables, code blocks, callouts, images, and Mermaid diagrams. Content authors can copy and paste examples from this template as a starting point for new UPNs.

This template has been created for reference purposes. None of the statements below reflect real product behavior.

---

<!-- A Table of Content is required for UPNs with greater than 900 words.
Use anchor links for navigation within the document.
UPNs published to the Academy will display a back to top button -->
### Table of contents

[Description](#description)

[Links](#links)

[Tables](#tables)

[Code blocks](#code-blocks)

[Images](#images)

[UPN Alert blocks](#upn-alert-blocks)

[Mermaid diagrams](#mermaid-diagrams)

---

### Description

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non nunc ac orci euismod pretium sit amet vitae sapien. Integer euismod, dui et porttitor dictum, purus justo mattis sem, non aliquet arcu tellus eget orci.

The following are samples of formatting that may be used in Update Note markdown.

#### Bulleted list <!-- In UPN MD Heading 4 is used for section sub headings -->
<!-- Bulleted lists will inherit the default markdown format-->
- Alpha item — short description text to test wrapping behavior in narrow viewports.
- Beta item — includes `inline code` for style confirmation.
- Gamma item — contains a longer run-on description to ensure hyphenation and spacing are handled gracefully across different rendering engines used in PDF export and HTML.
  - Nested bullet A
    - Nested bullet A.1
  - Nested bullet B
    - Nested bullet B.1

#### Numbered list
<!-- Numbered lists will inherit the default markdown format -->
1. First action the user might hypothetically take.
    1. Nested
    2. Example
        1. Another number
    3. List
2. Second action referencing an (imaginary) configuration screen.
3. Third action with an embedded note reference (see below).

#### Block quotes

You can turn text block into a quote

Text that is not a quote

> Text that is a quote

#### Fenced text block

```text
THIS IS PLACEHOLDER BLOCK TEXT
LINE TWO FOR WIDTH TESTING
LINE THREE WITH 1234567890 !@#$%^&*()
```

#### Inline Formatting

- **Bold**
- *italic*
- ***bold italic***
- `inline code`
- ~~strikethrough~~
- Special characters ^&%$#@! (sanitized before persistence)
- $_subscript$ and $^superscript$

#### Edge cases

| Scenario | Input | Expected (Conceptual) |
|----------|-------|-----------------------|
| Empty allocation | 0 | No event emitted |
| Large allocation | 999999 | Value accepted; triggers warning banner |
| Null reference | (null) | Validation error displayed |

### Links

[WiseTech Academy](https://wisetechacademy.com/)

`<link>` : <https://wisetechacademy.com/>

### Tables

#### Sample Table

| Field | Type | Example | Notes |
|-------|------|---------|-------|
| Id | GUID | `3f2504e0-4f89-11d3-9a0c-0305e82c3301` | Unique identifier placeholder |
| Name | String | Demo Console Name | Arbitrary text value |
| Quantity | Number | 42 | Edge case: zero / negative / large |
| Active | Boolean | true | Toggle rendering check |

#### Sample Table - Change history log

| Date | Version | Description of change |
|-------|------|---------|
| 7 Jan 2026 | 1.0 | Text aligned left |
| 31 Jan 2026 | 1.1 | Fig 1. Screenshot replace |

#### Additional syntax for complex tables

You can align text to the left, right, or center of a column by including colons : to the left, right, or on both sides of the hyphens within the header row.

| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| Text aligned left   | Text aligned center     | Text aligned right    |
| Left   | Center     | Right    |

For more complex tables, you can use unicode characters and HTML elements to influence column widths and text wrapping in complex cells. Using HTML tags makes the markdown harder to read and edit in raw form, so **should be avoided** but may be necessary.

Where necessary, you can use:

| Element | Usage |
| :-----: | :---- |
| `<br>` | to force line breaks within cells. |
| `&nbsp;` | non-breaking space used:<br> • instead of space to prevent words being wrapped.<br> • in grid headers to force more space in particular columns. |
| `•` | unicode bullet (0x2022) used after `<br>` to created dot point lists in a cell. |
| `‑` | unicode non-breaking hyphen (0x2011) to keep hyphenated words and number sequences like phone numbers together. |

Images and unicode bullets used in table cells <!-- See Read Me for guidance on sizing and saving images -->

| Element | Usage |
| :-----: | :---- |
| Image | Images will appear at there full width in the VS Code preview, they will be reduced to half size when published in the Academy. Use `<br>` to have the image appear on a new line or increase spacing. <br><br>![Test image for table insertion example](_images/Screenshot_Sm_Test.png) |
| Bullets in a cell   | non-breaking space used:<br> • instead of space to prevent words being wrapped.<br> • in grid headers to force more space in particular columns. |

> [!NOTE]
>
> The data contained in complex tables with few columns may be visually clearer and easier to navigate when broken up using H2 and H3 headings with repeating sets of dot points instead.

### Code blocks <!-- Dummy code examples for syntax block styling -->

#### Inline code

How to add `inline code` into text.

#### PowerShell

```powershell
$items = 1..5 | ForEach-Object { [PSCustomObject]@{ Index = $_; Timestamp = (Get-Date) } }
$items | Format-Table -AutoSize
```

#### JSON

```json
{
  "featureFlag": true,
  "maxItems": 100,
  "endpoints": ["/alpha","/beta","/gamma"],
  "metadata": { "environment": "test", "build": 1234 }
}
```

#### XML

```xml
<EventType>
<Code>ALD</Code>
<Description>Allocated</Description>
</EventType>
<EventTime>2025-07-02T11:44:59.203+10:00</EventTime>
<EventType>ALD</EventType>
<CreatedTime>2025-07-02T01:44:59.203+00:00</CreatedTime>
<EventReference>|CON=GSS|ORG=US10IMSEA|QTY=1.00|RFN=00000009|STA=NEW|TYP=TEU</EventReference>
Importing a Universal Event XML with 'ALD' as the 'Code' will not currently generate an 'ALD - Allocated' event. Support for this functionality is planned for future CargoWise releases.
```

### Images

See the Repository Read Me for guidance on how to create, resize and save images for use in UPNs.

![Dummy allocation illustration reusing existing test image](_images/Screenshot_Test.png)

> Fig 1. Use a block quote for captions.

### UPN Alert blocks

Alert blocks can be used to highlight important or critical information. These are visually distinct, featuring unique colors and icons to emphasize the significance of the content.

UPN callouts

The Update Notes use 3 alert block types NOTE, IMPORTANT, and ACTION. These examples show the code syntax and followed by an image of how the alert block will appear when published on the Academy.

> [!NOTE]
> This feature works the same way as the Send Password Instructions in CargoWise found in Organization > Contacts > Web Security > Send Password Instructions button.
>

![Notes box is a purple box with CargoWise blue text](_images/NOTE_Example.png)
> [!IMPORTANT]
> Staff security rights specific to this module OR the Controller role are required for a successful login. You will find more information on page 6 of this update note regarding granting the appropriate staff security rights.
>

![Notes box is a purple box with CargoWise blue text](_images/IMPORTANT_Example.png)
> [!ACTION] <!-- Note that ACTION will not render in the Markdown preview -->
> Do not copy this dummy content into production knowledge articles.

![Notes box is a purple box with CargoWise blue text](_images/ACTION_Example.png)

### Mermaid diagrams

#### Graph example

```mermaid
graph TD;
   A[Start] --> B{Decision}
   B -->|Yes| C[Do Task]
   B -->|No| D[End]
   ```

#### Sequence example

```mermaid
sequenceDiagram
participant Alice
participant Bob
Alice->>Bob: Hello Bob, how are you?
Bob-->>Alice: I am good, thanks!
```
