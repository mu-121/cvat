# Objectives

## Primary Objective

Build an annotation analytics feature in CVAT that returns the number
of annotations per class for a task and displays those counts as a graph.

## Measurable Performance Target

The annotation-count API should return a successful response in
under 500 ms for a task containing the assessment sample annotations,
measured across 5 consecutive requests.

The final report will record:

- Machine CPU
- Machine RAM
- Operating system
- CVAT commit SHA
- Dataset/image count
- Five raw request timings
- Median response time
- Response-time spread

## Additional Analytics Objective

Add one useful grouping/filter beyond the basic per-class count.

The selected grouping/filter will be documented together with why it
is useful for annotation review.

## Reliability Objective

The page should clearly handle:

- No annotation data
- Failed API requests
- Unauthorized task access
