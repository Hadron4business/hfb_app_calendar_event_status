# Calendar Meeting Status

Adds a status to calendar meetings (unconfirmed, confirmed, done, cancelled) with a cancellation reason.

## What it does

- **Four statuses** - Unconfirmed, Confirmed, Done and Cancelled, shown in a status bar on the meeting.
- **Cancellation reason** - Cancelling asks for a reason. It is stored on the meeting and written to the chatter.
- **Colored badges** - The meeting list shows the status as a colored badge.
- **Filter and group** - Find all open or cancelled meetings with ready-made filters and a group-by.
- **History** - Every status change is tracked in the chatter.
- **Reversible** - A meeting can be reopened or set back to Unconfirmed at any time.

## How to use it

1. Open Calendar and open any meeting (or create one). A status bar with buttons appears above the form.
2. A new meeting is Unconfirmed. Press Confirm when it is going ahead.
3. After the meeting press Set as Done.
4. To cancel, press Cancel, type the reason and press Cancel Meeting. The reason is shown on the meeting.
5. Press Set to Unconfirmed (or Confirm) to bring a cancelled meeting back.
6. In the list view of meetings use the filters Unconfirmed / Confirmed / Done / Cancelled or group by Meeting Status.

## Good to know

- Existing meetings become Unconfirmed when the app is installed.
- The status is separate from the attendees' answers (accepted / declined).
- Cancelling does not delete or archive the meeting and does not notify attendees.
- For a recurring event, each occurrence has its own status.

## Technical

- `models/calendar_event.py` - fields `meeting_state` and `cancel_reason` on `calendar.event`, status actions.
- `wizard/calendar_event_cancel.py` - transient model that asks for the reason.
- Views extend `calendar.view_calendar_event_form`, `view_calendar_event_tree` and `view_calendar_event_search`.
- Depends on: `calendar`.

## Status

Source: client module (Odoo 16, ported to 17), where the status was a few fields and a cancel form hacked into the calendar form. Rewritten with a proper wizard. Odoo 19 build.
