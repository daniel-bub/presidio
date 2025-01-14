# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]
### Changed

### Removed

### Deprecated

## [2.2.0] - 12.04.2021
### Changed
#### Analyzer:
Upgrade Analyzer spacy version to 3.0.5

#### Anonymizer Engine:
1. Request entity AnonymizerConfig renamed OperatorConfig
    - In OperatorConfig: anonymizer_name -> operator_name
2. Response entity AnonymizerResult renamed to EngineResult
    - In EngineResult: List[AnonymizedEntity] -> List[OperatorResult]
    - In OperatorResult: 
        - anonymizer -> operator
        - anonymized_text -> text

#### Anonymize API:
1. Response entity anonymizer renamed to operator.
2. Response entity anonymizer_text renamed to text.

#### Deanonymize:
New endpoint for deanonymizing encrypted entities by the anonymizer.

[unreleased]: https://github.com/microsoft/presidio/compare/2.2.0...HEAD
[2.2.0]: https://github.com/microsoft/presidio/compare/2.1.0...2.2.0
