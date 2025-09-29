# ToDo App: Epics and User Stories with Acceptance Criteria

This document outlines the high-level functional areas (**Epics**), the required user-facing features (**User Stories**), and the conditions for deeming each feature complete (**Acceptance Criteria**).

---

## Epic 1: Core Task Management (Minimum Viable Product)

This Epic covers the basic functionality required to create, view, and manipulate individual tasks.

| #  | User Story | Acceptance Criteria |
|----|------------|-------------------|
| 1  | As a user, I want to quickly add a new task so that I can capture an idea or chore before I forget it. | **GIVEN** I am on the main task view, **WHEN** I type text into the input field and press ENTER, **THEN** a new active task appears at the top of the list, AND the input field is cleared. |
| 2  | As a user, I want to see a list of all my tasks so that I know what work I have prioritized. | **GIVEN** I have multiple active and completed tasks, **WHEN** I open the app in the default view, **THEN** all tasks are visible and sorted by creation date (newest first). |
| 3  | As a user, I want to mark a task as complete so that I can track my progress and clean up my active list. | **GIVEN** I see an active task, **WHEN** I click the checkbox next to the task, **THEN** the task is visually struck through (or moves to the completed section) AND its status is updated in the database. |
| 4  | As a user, I want to be able to edit the text of an existing task so that I can correct typos or update details. | **GIVEN** an existing task, **WHEN** I double-click the task text, **THEN** the text becomes an editable field AND pressing ENTER or clicking away saves the new text and returns the task to view mode. |
| 5  | As a user, I want to delete a task permanently so that I can remove irrelevant or redundant items from my list. | **GIVEN** an existing task, **WHEN** I click the 'Delete' icon (e.g., trash can), **THEN** the task is immediately removed from the visible list and the persistence layer. |
| 6  | As a user, I want the app to save my tasks automatically so that my data is persistent when I close and re-open the application. | **GIVEN** I add or modify a task, **WHEN** I close and reopen the app, **THEN** the application loads the last saved state of all tasks (active/completed) without user intervention. |
| 7  | As a user, I want to view only my active (uncompleted) tasks so that I can focus on my immediate priorities. | **GIVEN** I click the "Active" filter button/tab, **THEN** only tasks that are NOT marked complete are shown. |
| 8  | As a user, I want to view only my completed tasks so that I can review past accomplishments. | **GIVEN** I click the "Completed" filter button/tab, **THEN** only tasks that ARE marked complete are shown. |

---

## Epic 2: Task Organization and Filtering

This Epic focuses on tools that help users manage a growing number of tasks efficiently.

| #  | User Story | Acceptance Criteria |
|----|------------|-------------------|
| 9  | As a user, I want to assign a due date to a task so that I know exactly when it needs to be finished. | **GIVEN** an existing task, **WHEN** I click the "Add Due Date" button, **THEN** a calendar picker appears AND selecting a date displays the date next to the task. |
| 10 | As a user, I want to sort my tasks by their due date so that I can prioritize what is coming up next. | **GIVEN** tasks with different due dates, **WHEN** I select the 'Sort by Due Date' option, **THEN** tasks with the earliest due date appear at the top. |
| 11 | As a user, I want to assign a priority level (High, Medium, Low) so that I can quickly identify the most critical items. | **GIVEN** an existing task, **WHEN** I click the priority icon, **THEN** I can select High, Medium, or Low AND the task displays a visible indicator (color or flag) reflecting the chosen priority. |
| 12 | As a user, I want to filter tasks by priority level so that I can work only on my 'High' priority items. | **GIVEN** I click the 'Priority' filter and select 'High', **THEN** only tasks marked 'High' are visible. |
| 13 | As a user, I want to group tasks into different 'Lists' or 'Projects' so that I can separate personal chores from work-related items. | **GIVEN** I select a task, **WHEN** I assign it to a 'Project' list (e.g., "Work"), **THEN** I can view a separate list page showing only "Work" tasks. |
| 14 | As a user, I want to quickly search for tasks using keywords so that I can find a specific item without scrolling through a long list. | **GIVEN** I type text into the search bar, **WHEN** I have tasks matching that text, **THEN** the list immediately updates to show only the tasks whose name contains the entered text (case-insensitive). |

---

## Epic 3: User Experience and Accessibility

This Epic includes features focused on polish, interaction quality, and visual comfort.

| #  | User Story | Acceptance Criteria |
|----|------------|-------------------|
| 15 | As a user, I want to see a counter of my active tasks so that I have a quick overview of my remaining workload. | **GIVEN** there are N active tasks, **THEN** a visible number or badge displays the accurate number "N Active Tasks" and updates instantly when a task is completed or added. |
| 16 | As a user, I want an option to clear all completed tasks at once so that I can easily tidy up my completed list. | **GIVEN** I have completed tasks, **WHEN** I click the "Clear Completed" button, **THEN** a confirmation modal appears, AND confirming the action permanently deletes all completed tasks. |
| 17 | As a user, I want to use a Dark Mode setting so that I can use the application comfortably in low-light environments. | **GIVEN** I toggle the 'Dark Mode' switch in the settings, **THEN** the app's background changes to a dark color and the text changes to a light color across all screens. |
| 18 | As a user, I want an 'Undo' button after deleting a task so that I can quickly recover a task I removed by mistake. | **GIVEN** I just deleted Task A, **THEN** a transient "Undo" toast notification appears for 5 seconds, AND clicking "Undo" restores Task A to its previous state and position in the list. |

---

## Epic 4: Notifications and Reminders

This Epic is dedicated to features that help the user stay on top of their commitments.

| #  | User Story | Acceptance Criteria |
|----|------------|-------------------|
| 19 | As a user, I want to receive a push notification when a task is due in the next hour so that I don't miss important deadlines. | **GIVEN** the task has a due date set AND the app is running in the background, **THEN** a system notification is sent to the user's device 60 minutes before the due time. |
| 20 | As a user, I want to customize the reminder time for a task (e.g., 1 day before, 2 hours before) so that I get alerted at the right time for that specific item. | **GIVEN** I set a task's due date, **WHEN** I select a reminder offset (e.g., "2 hours before"), **THEN** a notification is scheduled for the time calculated by the offset relative to the due date. |
