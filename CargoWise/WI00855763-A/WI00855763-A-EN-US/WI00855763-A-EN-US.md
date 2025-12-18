---
###########################################################################################################
# This is the official update note template, all future templates should be based on this as a reference. #
###########################################################################################################

# Required front matter in YAML
published: true                     # Reviewer use only, determines if the UPN should be published or not. False if not.
title: Document Title               # Not to be confused with the filename, this will be used specifically for the label on the link
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

## Summary

The following section contains intentionally fabricated content for layout, styling, callout, link, table, list, code, and media regression testing. None of the statements below reflect real product behavior. You can freely remove this entire section once testing is complete.

#### Placeholder Paragraphs

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non nunc ac orci euismod pretium sit amet vitae sapien. Integer euismod, dui et porttitor dictum, purus justo mattis sem, non aliquet arcu tellus eget orci.

Curabitur at nisl nec sapien pretium rhoncus. Suspendisse potenti. Etiam euismod, nisl quis aliquet efficitur, augue magna tempor lorem, vitae aliquet urna orci ac nisl.

#### Bulleted List Example

- Alpha item — short description text to test wrapping behavior in narrow viewports.
- Beta item — includes `inline code` for style confirmation.
- Gamma item — contains a longer run-on description to ensure hyphenation and spacing are handled gracefully across different rendering engines used in PDF export and HTML.
  - Nested bullet A
    - Nested bullet A.1
  - Nested bullet B
    - Nested bullet B.1

#### Numbered List Example

1. First action the user might hypothetically take.
    1. Nested
    2. Example
        1. Another number
    3. List
2. Second action referencing an (imaginary) configuration screen.
3. Third action with an embedded note reference (see below).

#### Definition Style (Pseudo)

Term One  
: Definition or elaboration for term one used to test soft line breaks.  
Term Two  
: Follow-up explanation with additional dummy narrative.

#### Sample Table

| Field | Type | Example | Notes |
|-------|------|---------|-------|
| Id | GUID | `3f2504e0-4f89-11d3-9a0c-0305e82c3301` | Unique identifier placeholder |
| Name | String | Demo Console Name | Arbitrary text value |
| Quantity | Number | 42 | Edge case: zero / negative / large |
| Active | Boolean | true | Toggle rendering check |

#### Code Samples

PowerShell example:

```powershell
# Dummy PowerShell to test syntax block styling
$items = 1..5 | ForEach-Object { [PSCustomObject]@{ Index = $_; Timestamp = (Get-Date) } }
$items | Format-Table -AutoSize
```

JSON configuration snippet:

```json
{
  "featureFlag": true,
  "maxItems": 100,
  "endpoints": ["/alpha","/beta","/gamma"],
  "metadata": { "environment": "test", "build": 1234 }
}
```

XML fragment:

```xml
<DummyEvent code="ZZZ" status="TEST">
  <Detail>Lorem ipsum placeholder</Detail>
  <Value unit="TEU">0</Value>
</DummyEvent>
```

#### Image Reference (Existing Asset)

![Dummy allocation illustration reusing existing test image](images/Screenshot_Sm_Test.png)

#### Mixed Callouts

> [!NOTE]
> This is purely fictitious and safe to delete.
>
> [!IMPORTANT]
> Ensure downstream pipelines ignore this section for release notes.
>
> [!ACTION]
> Do not copy this dummy content into production knowledge articles.

#### Fenced Text Block

```text
THIS IS PLACEHOLDER BLOCK TEXT
LINE TWO FOR WIDTH TESTING
LINE THREE WITH 1234567890 !@#$%^&*()
```

#### Edge Case Examples

| Scenario | Input | Expected (Conceptual) |
|----------|-------|-----------------------|
| Empty allocation | 0 | No event emitted |
| Large allocation | 999999 | Value accepted; triggers warning banner |
| Null reference | (null) | Validation error displayed |
| Special chars | ^&%$#@! | Sanitized before persistence |

#### Inline Formatting Matrix

Bold, _italic_, **_bold italic_**, `inline code`, ~~strikethrough~~, and a [dummy link](https://example.test/placeholder) for crawler sanity.
 $_subscript$ and $^superscript$
