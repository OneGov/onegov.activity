Changelog
---------
1.19.2 (2019-05-21)
~~~~~~~~~~~~~~~~~~~
1.19.1 (2019-05-21)
~~~~~~~~~~~~~~~~~~~

- Fixes anti-affinity group being checked by default.

  It is only necessary to do so during matching.
  [href]

1.19.0 (2019-05-15)
~~~~~~~~~~~~~~~~~~~

- Adds a more flexible age-barrier check system.
  [href]

1.18.4 (2019-05-14)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to check if an invoice has a donation or not.
  [href]

1.18.3 (2019-05-07)
~~~~~~~~~~~~~~~~~~~

- Adds a stop-gap measure to the occasion-period-change regression.

  In this regression it was possible to reassign occasions to different periods
  even if bookings have already been made. This stop gap excludes all such
  bookings from matching that can be reliably detected as such.

1.18.2 (2019-04-15)
~~~~~~~~~~~~~~~~~~~

- Adds helper methods to check for disabled/discouraged changes on invoice items.
  [href]

1.18.1 (2019-04-13)
~~~~~~~~~~~~~~~~~~~

- Improves robustness of activity filters when facing invalid parameters.
  [href]

1.18.0 (2019-04-12)
~~~~~~~~~~~~~~~~~~~

- Improves control over invoice session flushing.
  [href]

- Removes occasion.active.
  [href]

- Removes invoice.code.
  [href]

1.17.2 (2019-03-19)
~~~~~~~~~~~~~~~~~~~

- Fixes matching with affinity groups leading to invalid outcomes.
  [href]

1.17.1 (2019-03-12)
~~~~~~~~~~~~~~~~~~~

- Fixes 'free occasions' price filter not working as intended.
  [href]

- Fixes ISO20022 matching not working in some cases.
  [href]

1.17.0 (2019-02-25)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to show the available ages for all activities.
  [href]

1.16.0 (2019-02-21)
~~~~~~~~~~~~~~~~~~~

- Stores the calculate score on each booking.
  [href]

1.15.1 (2019-02-20)
~~~~~~~~~~~~~~~~~~~

- Fixes activity names with numbers leading to errors.
  [href]

1.15.0 (2019-02-20)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to exempt occasions from booking limits.
  [href]

1.14.1 (2019-02-19)
~~~~~~~~~~~~~~~~~~~

- Fixes faulty release.
  [href]

1.14.0 (2019-02-19)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to define needs for occasions.
  [href]

1.13.0 (2019-02-16)
~~~~~~~~~~~~~~~~~~~

- Supports smaller Raiffeisen ESR identifications.
  [href]

- Prefers groups in the matching algorithm.
  [href]

- Adds the ability to book multiple occasions from one activity.
  [href]

- Adds a cancellation deadline to the period.
  [href]

1.12.1 (2019-02-11)
~~~~~~~~~~~~~~~~~~~

- Fixes a number of issues with the invoice reference implementation.
  [href]

1.12.0 (2019-02-08)
~~~~~~~~~~~~~~~~~~~

- Adds invoice references to support more banks.
  [href]

1.11.0 (2019-02-07)
~~~~~~~~~~~~~~~~~~~

- Groups invoice items under an invoice record.
  [href]

1.10.3 (2018-10-29)
~~~~~~~~~~~~~~~~~~~

- Fixes tests.
  [href]

1.10.2 (2018-10-12)
~~~~~~~~~~~~~~~~~~~

- Improves the 'undated' filter to work with the selected periods.
  [href]

1.10.1 (2018-09-24)
~~~~~~~~~~~~~~~~~~~

- Adds filtering activites by occasions (now, future, past, without).
  [href]

1.10.0 (2018-09-22)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to filter activities by price range.
  [href]

- Completely reworks the way activities are filtered, taking the periods
  properly into account.
  [href]

- Moves activity filters to a separate object.
  [href]

1.9.0 (2018-08-21)
~~~~~~~~~~~~~~~~~~~

- Adds a flag indicating that the organiser should be paid directly.
  [href]

1.8.2 (2018-08-02)
~~~~~~~~~~~~~~~~~~~

- Ignores invalid values passed to the activity collection instead of raising.
  [href]

1.8.1 (2018-05-08)
~~~~~~~~~~~~~~~~~~~

- Improves matching performance.
  [href]

1.8.0 (2018-04-16)
~~~~~~~~~~~~~~~~~~~

- Counts activities with multi-date occasions as multi-date.
  [href]

1.7.3 (2018-03-13)
~~~~~~~~~~~~~~~~~~~

- Categorises occasions as spanning multiple days more eagerly.
  [href]

1.7.2 (2018-03-08)
~~~~~~~~~~~~~~~~~~~

- Fixes an exception occuring during certain matching runs.
  [href]

1.7.1 (2018-02-21)
~~~~~~~~~~~~~~~~~~~

- Allows changes on refunded or failed online payments.
  [href]

1.7.0 (2018-02-20)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to limit attendees to one activity per day.
  [href]

1.6.2 (2018-02-19)
~~~~~~~~~~~~~~~~~~~

- Adds a subscription token to the attendee.
  [href]

1.6.1 (2018-02-12)
~~~~~~~~~~~~~~~~~~~

- Adds an available_weeks function to the actiity collection.
  [href]

1.6.0 (2018-01-22)
~~~~~~~~~~~~~~~~~~~

- Adds family column.
  [href]

- Requires Python 3.6.
  [href]

1.5.1 (2017-12-05)
~~~~~~~~~~~~~~~~~~~

- No longer raises an error when a proposed activity is proposed again.
  [href]

1.5.0 (2017-10-16)
~~~~~~~~~~~~~~~~~~~

- Changes the activity filter to have more useful options.
  [href]

- Adds some matching of manual payments to iso20022 matcher.
  [href]

- Adds the ability to filter activities by availability.
  [href]

- Counts available spots as 0 if the occasion has been cancelled.
  [href]

1.4.0 (2017-10-11)
~~~~~~~~~~~~~~~~~~~

- Adds a municipality field to activities.
  [href]

1.3.0 (2017-10-10)
~~~~~~~~~~~~~~~~~~~

- Make invoice items payable.
  [href]

1.2.3 (2017-09-26)
~~~~~~~~~~~~~~~~~~~

- Switches to onegov.search's automatic language detection.
  [href]

1.2.2 (2017-09-21)
~~~~~~~~~~~~~~~~~~~

- Adds support for LXML 4.0.
  [msom]

1.2.1 (2017-08-03)
~~~~~~~~~~~~~~~~~~~

- Adds support for Camt.054.
  [href]

1.2.0 (2017-06-22)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to archive a period.
  [href]

- Adds a publication request to allow activities to be attached to tickets
  at least once per period.
  [href]

1.1.0 (2017-06-21)
~~~~~~~~~~~~~~~~~~~

- Automatically extracts a single thumbnail from activity descriptions.
  [href]

1.0.0 (2017-05-29)
~~~~~~~~~~~~~~~~~~~

- Bumps version to 1.0.0.
  [href]

0.8.10 (2017-05-19)
~~~~~~~~~~~~~~~~~~~

- Fixes activity collection pagination not recognizing the active element.
  [href]

0.8.9 (2017-05-12)
~~~~~~~~~~~~~~~~~~~

- The deadline is now inclusive (including the day it ends) for dates.
  [href]

0.8.8 (2017-05-12)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to filter the activities by weekday.
  [href]

0.8.7 (2017-05-10)
~~~~~~~~~~~~~~~~~~~

- Consider all bookings for matchings except for the cancelled ones.
  [href]

- Adds a method to check if an activity has an occasion in a given period.
  [href]

- Adds helper methods for prebooking checks (before, during, after).
  [href]

0.8.6 (2017-05-08)
~~~~~~~~~~~~~~~~~~~

- Adds a relationship between invoice_item and user.
  [href]

0.8.5 (2017-05-08)
~~~~~~~~~~~~~~~~~~~

- Encodes the period bound booking state on the booking.
  [href]

0.8.4 (2017-05-04)
~~~~~~~~~~~~~~~~~~~

- Adds support for ESR reference numbers in payments.
  [href]

0.8.3 (2017-05-02)
~~~~~~~~~~~~~~~~~~~

- Adds elasticsearch indexing to the attendees (private only).
  [href]

0.8.2 (2017-04-11)
~~~~~~~~~~~~~~~~~~~

- Fixes reference code in ISO20022 statements not being detected in some cases.
  [href]

0.8.1 (2017-03-23)
~~~~~~~~~~~~~~~~~~~

- Fixes accept_booking falsly claiming a booking was in conflict.
  [href]

0.8.0 (2017-03-14)
~~~~~~~~~~~~~~~~~~~

- Removes the 'denied' state for activities.
  [href]

- Adds the ability to cancel a booking without cascading changes.
  [href]

- Check the booking limit of the attendee when accepting a booking.
  [href]

0.7.0 (2017-03-02)
~~~~~~~~~~~~~~~~~~~

- Adds active days to the activity/occasion models.
  [href]

- Fix age calcualation not being correct on some birthdays.
  [href]

- Fixes activity delete not working if there are attached occasions.
  [href]

0.6.3 (2017-02-28)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to nobble bookings.
  [href]

0.6.2 (2017-02-27)
~~~~~~~~~~~~~~~~~~~

- Adds user reference to bookings and attendees.
  [href]

0.6.1 (2017-02-24)
~~~~~~~~~~~~~~~~~~~

- Adds a meeting point to the occasion, a location to the activity.
  [href]

- Adds the ability to filter the booking counts per username by state.
  [href]

0.6.0 (2017-02-24)
~~~~~~~~~~~~~~~~~~~

- Adds attendee-based limits.
  [href]

- Adds a way to control the deadline to the period.
  [href]

0.5.1 (2017-02-21)
~~~~~~~~~~~~~~~~~~~

- Enable state changes to all states except to the proposed state.
  [href]

0.5.0 (2017-02-16)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to exclude certain occasions from overlapping with others.
  [href]

- Adds the ability to enforce time between occasions during matching.
  [href]

- Fixes stability check not working correctly with cascades.
  [href]

0.4.2 (2017-02-15)
~~~~~~~~~~~~~~~~~~~

- Adds a helper method to verify a given birth date's age for an occasion.
  [href]

0.4.1 (2017-02-14)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to clear all dates of an occasion.
  [href]

0.4.0 (2017-02-09)
~~~~~~~~~~~~~~~~~~~

- Reworks the occasions database model to include multiple dates per occasion.
  [href]

- Do not start the wishlist-phase before its start date.
  [href]

- Adds a notes field to the attendees.
  [href]

- Adds a gender field to the attendees.
  [href]

0.3.0 (2017-01-30)
~~~~~~~~~~~~~~~~~~~

- Adds a source field to the invoice items to note the source of the tid.
  [href]

- Adds a simple ISO20022 parser to process payments.
  [href]

- Adds a code field to the invoice items for online banking reference.
  [href]

0.2.0 (2016-12-13)
~~~~~~~~~~~~~~~~~~~

- Adds an 'outstanding' property to the invoice item collection.
  [href]

- Adds the ability to cancel an occasion.
  [href]

- Make sure direct bookings have the correct cost set.
  [href]

0.1.2 (2016-12-01)
~~~~~~~~~~~~~~~~~~~

- Adds columns for payment/booking costs.
  [href]

- Adds the ability to limit the number of matched bookings.
  [href]

- Adds the ability to create invoices for bookings.
  [href]

- Fixes matching resulting in an error in certain constellations.
  [href]

0.1.1 (2016-11-25)
~~~~~~~~~~~~~~~~~~~

- Adds a finalized flag to the periods which indicates that the period
  transitioned from the booking to the payment phase.
  [href]

- Adds the ability to accept/cancel bookings in a confirmed period.
  [href]

- Adds an accepted booking count to the occasion, along with properties to
  check for operable and/or full occasions.
  [href]

- Adds a custom data column to the period.
  [href]

- Introduces the ability to configure custom scoring functions for matching.
  [href]

- Starring a booking no longer leads to a cascade of updates.
  [href]

0.1.0 (2016-11-18)
~~~~~~~~~~~~~~~~~~~

- Periods now have a confirmed flag. Confirmed periods can be booked directly,
  while unconfirmed bookings an be booked through the wishlist and matched
  using the matching algorithm.
  [href]

- Adds an implementation of Deferred Acceptance as a matching algorithm.
  [href]

- Introduces a happiness function on the attendee which returns a value
  between 0.0 and 1.0 depending on how happy the attendee is assumed to be
  with the bookings confirmed for the given period.
  [href]

- Adds the denormalized period_id to the bookings.
  [href]

- Make sure all models are hashable.
  [href]

0.0.11 (2016-11-02)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to star/unstar a booking.
  [href]

- Adds the ability to switch the username or period on the bookings collection.
  [href]

- Adds the ability to filter the bookings by username or period.
  [href]

- Includes a count method for bookings per user.
  [href]

- Adds an attendee model.
  [href]

0.0.10 (2016-10-20)
~~~~~~~~~~~~~~~~~~~

- Reworks the datamodel to include a period linked to the occasion/bookings.
  [href]

0.0.9 (2016-10-17)
~~~~~~~~~~~~~~~~~~~

- Improves the performance of the used_tags method.
  [href]

0.0.8 (2016-10-14)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to filter the activites by one or many owners.
  [href]

- Adds the ability to filter the activites by age ranges.
  [href]

0.0.7 (2016-10-10)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to filter activites by the duration of their occasions.
  [href]

- Adds a db constraint ensuring that an occasion always starts before it ends.
  [href]

- Adds an archived state to occasions.
  [href]

0.0.6 (2016-10-06)
~~~~~~~~~~~~~~~~~~~

- Adds a reporter column to activites.
  [href]

0.0.5 (2016-10-04)
~~~~~~~~~~~~~~~~~~~

- Occasions and bookings can no longer be orphaned.
  [href]

- Location is now optional.
  [href]

- Adds an occasion collection.
  [href]

0.0.4 (2016-10-03)
~~~~~~~~~~~~~~~~~~~

- Overhauls the occasion model.
  [href]

0.0.3 (2016-09-29)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to directly access the user object from the activity.
  [href]

0.0.2 (2016-09-26)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to override the query base on a subclass.
  [href]

- Adds the ability to filter the collection by state.
  [href]

- Adds the ability to get the set of used activity tags.
  [href]

0.0.1 (2016-09-22)
~~~~~~~~~~~~~~~~~~~

- Initial Release
