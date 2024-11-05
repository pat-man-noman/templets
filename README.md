# Module 2: Templates

## Videos

1. [Responding with HTML](./videos/responding_with_html.mp4)
2. [Templates over Data](./videos/templates_over_data.mp4)
3. [Static Assets and CSS](./videos/static_assets_and_css.mp4)
4. [Path names and `url`](./videos/path_names_and_url.mp4)
5. [Template Inheritance](./videos/template_inheritance.mp4)

## Exercises

Follow the steps below to build a BCCA Leadership Project Team Viewer.

### Step 1

With simple templates (like video 1), create the following pages:

- `/` should show a list of each project team names.
- `/management` should show detailed information about the management team.
- `/procurement` should show detailed information about the procurement team.
- Continue this for all of the remaining leadership project teams.

At the end of this step you should have:

- [ ] A path (`/`), view, and template for the team list page.
- [ ] Each team should have its own path, view, and template.
  - The path should be the name of the team.

### Step 2

Refactor the Team Detail pages to be a single view and template. Create a dataclass `Team` that represents all of the information about each team. Hint: you can use a `Dict[str, Team]` for easy lookup in your view.

At the end of this step you should have:

- [ ] A `Team` dataclass for representing each team.
  - It should at least contain the name of the team, a description, and a list of team member names.
- [ ] You should only have 1 path, view, and template for the team detail page.
  - The view should use a data structure to look up the appropriate `Team`.

### Step 3

Add some CSS! Your CSS must be linked correctly and served as a static file.

### Step 4

Add navigation with appropriate path name usage. You should have two paths with reasonable names and your templates should generate the correct links with the `url` template tag.

### Step 5

Refactor the project to share a base template between the list page and detail page.

## Mastery Check (Benchmark)

You will be asked to create a django project (and app) that allows the user to view some simple information about a domain.
