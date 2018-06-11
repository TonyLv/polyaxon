import tracker

from event_manager.events import build_job

tracker.subscribe(build_job.BuildJobCreatedEvent)
tracker.subscribe(build_job.BuildJobUpdatedEvent)
tracker.subscribe(build_job.BuildJobStartedEvent)
tracker.subscribe(build_job.BuildJobStartedTriggeredEvent)
tracker.subscribe(build_job.BuildJobSoppedEvent)
tracker.subscribe(build_job.BuildJobSoppedTriggeredEvent)
tracker.subscribe(build_job.BuildJobViewedEvent)
tracker.subscribe(build_job.BuildJobNewStatusEvent)
tracker.subscribe(build_job.BuildJobFailedEvent)
tracker.subscribe(build_job.BuildJobSucceededEvent)
tracker.subscribe(build_job.BuildJobDeletedEvent)
tracker.subscribe(build_job.BuildJobDeletedTriggeredEvent)
