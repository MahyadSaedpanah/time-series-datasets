# Contributing

Thanks for helping improve the Time Series Dataset Hub.

## Before submitting

Please check that the resource:

- is genuinely time-series data, an archive, or a time-series benchmark;
- has a canonical or primary source where possible;
- is not already represented under another name;
- has identifiable license/access terms;
- has accurate task/domain metadata;
- includes a paper, DOI, or official documentation link when available.

## Preferred source order

1. Official dataset or institutional page.
2. DOI / publisher / research-group repository.
3. Official competition page.
4. Official author repository.
5. Well-documented mirror only if the original distribution is unavailable.

## Adding an entry

1. Add one row to `datasets.csv`.
2. Follow [`docs/SCHEMA.md`](docs/SCHEMA.md).
3. Set `last_verified` to the date you checked the upstream source.
4. Run:

```bash
python scripts/validate_catalog.py
python scripts/build_readme.py
python scripts/build_readme.py --check
```

## Quality rules

- **Unknown is better than guessed.**
- Do not infer dataset licensing from code licensing.
- Avoid marketing language.
- Keep notes factual and short.
- Prefer exact sampling information where the source provides it.
- Keep each pull request focused.

## Pull request checklist

- [ ] I checked for duplicates.
- [ ] I used a canonical or primary source where possible.
- [ ] I verified the source URL.
- [ ] I included license/access information.
- [ ] I added a citation URL when available.
- [ ] I updated `last_verified`.
- [ ] Catalog validation passes.
- [ ] README generation check passes.
