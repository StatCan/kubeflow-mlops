import os
import json
from event_handler.dispatch import BaseDispatchEventHandler


class StartEventHandler(BaseDispatchEventHandler):

    MODEL_START_COMMENT = \
        "Model training has started\n" \
        "Run ID: {run_id}\n" \
        "See details at: [link]({run_link})\n" \
        "Commit sha: {sha}" \

    CHECK_RUN_NAME = "Model Training"
    CHECK_RUN_TITLE = "Model Training Pipeline"
    CHECK_RUN_SUMMARY = "In Progress"
    CHECK_RUN_TEXT = "See details at {}"

    def dispatch(self):
        run_link = os.getenv("KFP_DSHB") + "/_/pipeline/#/runs/details/" + self.run_id
        message = self.MODEL_START_COMMENT.format(
            run_id=self.run_id,
            sha=self.sha,
            run_link=run_link
        )

        self.add_comment(message)
        
        check_run_text = self.CHECK_RUN_TEXT.format(
            run_link)
        self.create_check_run(
            self.CHECK_RUN_NAME, self.CHECK_RUN_TITLE, self.CHECK_RUN_SUMMARY, check_run_text)
