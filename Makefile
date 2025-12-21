run-pipeline:
	dvc repro > logs/pipeline.log 2>&1
	echo "Pipeline finished. See logs/pipeline.log"
