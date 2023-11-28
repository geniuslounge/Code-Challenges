---
name: Custom issue template
about: Describe this issue template's purpose here.
title: ''
labels: 'Suggestions'
assignees: ''

---

body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report!
  - type: textarea
    id: title
    attributes:
      label: Title
      description: A short description of the code project
      placeholder: Enter a title
      value: ""
    validations:
      required: true
  - type: textarea
    id: description
    attributes:
      label: Description
      description: Tell us a bit more (full instructions here)
      placeholder: Tell us what to do!
      value: "Go build this thing that does this..."
    validations:
      required: true

