from cicd_templates_9b06fa8f.common import Job


class SampleJob(Job):
    def launch(self):
        self.logger.info("Launching bootstrap job")

        df = self.spark.range(0, 1000)

        df.write.format(self.conf["output_format"]).mode("overwrite").save(self.conf["output_path"])

        self.logger.info("Bootstrap job finished!")

if __name__ == "__main__":
    job = SampleJob()
    job.launch()
