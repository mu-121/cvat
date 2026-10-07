# Definition of Done

## Documentation

- [ ] Plan is committed before implementation work.
- [ ] Objectives are measurable and include a performance target.
- [ ] Definition of Done is committed before implementation work.

## Backend API

- [ ] API accepts a CVAT task ID.
- [ ] API reads annotation data from the database.
- [ ] API returns annotation counts grouped by class.
- [ ] API requires an authenticated CVAT user.
- [ ] API rejects unauthenticated requests.
- [ ] API rejects users without access to the requested task.

## Frontend

- [ ] Web page calls the annotation analytics API.
- [ ] Counts are displayed as a graph.
- [ ] Empty/no-data state is handled.
- [ ] Failed API request state is handled.

## Additional Analytics

- [ ] One useful grouping or filter beyond basic class count is implemented.
- [ ] The reason for the selected grouping/filter is documented.

## Performance

- [ ] One measurable API speed target is defined.
- [ ] Five measurements are recorded.
- [ ] Median response time is reported.
- [ ] Response-time spread is reported.
- [ ] CPU, RAM, OS, CVAT commit SHA, and dataset/image count are recorded.

## Live Updates

- [ ] Graph updates through WebSocket when annotations change.
- [ ] Page recovers after a dropped/reconnected WebSocket connection.
- [ ] If unfinished, the limitation and reason are documented.

## Testing

- [ ] Successful API response is tested.
- [ ] No-data case is tested.
- [ ] Failed request is tested.
- [ ] Authentication/authorization behavior is tested.
- [ ] Frontend graph behavior is checked.

## Submission

- [ ] Changes are committed in meaningful progress commits.
- [ ] Final branch is `dev-test01`.
- [ ] Exactly three required documents exist under `docs/`.
- [ ] Loom walkthrough is recorded and is no longer than 5 minutes.
- [ ] Final PR is opened from `dev-test01` into `main` of the personal fork.
- [ ] PR is not opened against the real CVAT repository.

## Evidence

Completed items will be checked off with test results, measurements,
screenshots, commit references, or other evidence where appropriate.

Unfinished items will be explicitly listed rather than marked complete.

