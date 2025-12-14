---
author: "Alejandro Munoz"
status: "Draft"
document_version: "Is this different to the software version?"
type: "update-note"
title: "New ALD – Allocated Event added for Consol utilizing Carrier Contract Allocations"
product: "CargoWise"
module: "Tariffs & Rates / Forwarding"
summary: Should this be included in the header?
language: "English"
search_terms: ""
release_date: ""
reissue_date: ""
published_date: ""
duration: ""
course_series: "Product learning"
membership_level: "Software User"
software_version: ""
---
### Dummy Data (Test Content)

The following section contains intentionally fabricated content for layout, styling, callout, link, table, list, code, and media regression testing. None of the statements below reflect real product behavior. You can freely remove this entire section once testing is complete.

#### Placeholder Paragraphs

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non nunc ac orci euismod pretium sit amet vitae sapien. Integer euismod, dui et porttitor dictum, purus justo mattis sem, non aliquet arcu tellus eget orci.

Curabitur at nisl nec sapien pretium rhoncus. Suspendisse potenti. Etiam euismod, nisl quis aliquet efficitur, augue magna tempor lorem, vitae aliquet urna orci ac nisl.

#### Bulleted List Example

- Alpha item — short description text to test wrapping behavior in narrow viewports.
- Beta item — includes `inline code` for style confirmation.
- Gamma item — contains a longer run-on description to ensure hyphenation and spacing are handled gracefully across different rendering engines used in PDF export and HTML.
  - Nested bullet A
  - Nested bullet B

#### Numbered List Example

1. First action the user might hypothetically take.
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
| Name | String | Demo Consol Name | Arbitrary text value |
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
<small>Caption: Reused small screenshot for dummy validation.</small>

#### Mixed Callouts

> [!NOTE]
> This is purely fictitious and safe to delete.
>
> [!TIP]
> Combine multiple callouts to confirm vertical spacing.
>
> [!IMPORTANT]
> Ensure downstream pipelines ignore this section for release notes.
>
> [!WARNING]
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

#### Cleanup Instruction

Remove everything from the heading "Dummy Data (Test Content)" downward when real content is ready.

***

End of dummy data section.
