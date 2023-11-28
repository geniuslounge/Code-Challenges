---
name: Code Challenge Submission
about: Propose a new code challenge to us.
title: 'Code Challenge Submission:'
labels: 'Suggestions'
assignees: 'trtmn'
body:
- type: markdown
  attributes:
    value: "## Welcome!"
- type: input
  id: title_of_challenge
  attributes:
    label: "Title of Challenge"
    description: "Succinct title for the challenge"
    placeholder: "Shuffle a deck of cards"
  validations:
    required: true
- type: textarea
  id: challenge_description
  attributes:
    label: "Challenge Description"
    description: "In more detail, give the instructions for the challenge here. Include demo data if needed"
    placeholder: "Create a deck of cards. Use classes, and methods that would commonly be used.
  validations:
    required: true
- type: dropdown
  id: difficulty
  attributes:
    label: Difficulty of Challenge
    options:
      - Easy
      - Medium
      - Hard
      - FML
  validations:
    required: true
  
  

---
