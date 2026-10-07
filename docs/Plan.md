# Plan

## Goal

Add annotation analytics to CVAT by building an API that returns
per-class annotation counts for a task and a web page that displays
those counts as a graph.

## Order of Work

1. Set up and verify the local CVAT Docker environment.
2. Import the COCO 2017 validation sample dataset and create a task
   containing labelled annotations.
3. Create the Django `test` app for the backend work.
4. Implement an authenticated API endpoint that:
   - accepts a task ID,
   - verifies the logged-in user can access the task,
   - reads annotation data from the database,
   - returns annotation counts grouped by class.
5. Add a frontend page that calls the endpoint and displays the counts
   as a graph.
6. Handle the empty-data and failed-request states.
7. Add one useful grouping/filter beyond the basic class count.
8. Define and measure one endpoint performance target using five runs.
9. If the core requirements are stable and time remains, implement
   live WebSocket updates and reconnect handling.
10. Run final checks, document evidence, record the walkthrough, and
    prepare the pull request.

## Time Plan

- Environment and sample data: 60 minutes
- Plan/documentation setup: 20 minutes
- Backend API: 90 minutes
- Frontend page and graph: 90 minutes
- Empty/error/access handling: 45 minutes
- Performance measurement and extra grouping/filter: 45 minutes
- WebSocket live updates: 60 minutes if time allows
- Final testing, documentation, recording, and submission: 50 minutes

## Intentionally Deferred

The WebSocket live-update requirement will only be attempted after
requirements 1–4 are complete and working. If time becomes limited,
WebSocket live updates and reconnect handling will be left unfinished
and documented rather than rushed.

## Evidence

The Definition of Done will contain evidence for completed requirements,
including test results, measurements, and links or references where
appropriate.
