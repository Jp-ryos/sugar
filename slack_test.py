import slackweb

slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
slack.notify(text="hello world")
