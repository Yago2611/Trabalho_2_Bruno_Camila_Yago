
import sys
from src.datasets.dataset_factory import create_dataset
from src.classifiers.classifier_factory import create_classifier
from src.experiment import Experiment
from src.io.config import load_config
from src.io.report import write_report


def main():
    args = sys.argv
    config = load_config(args[1])

    train_config = config['train_dataset']
    test_config = config['test_dataset']
    classifier_config = config['classifier']

    train_dataset = create_dataset(train_config["path"], train_config["type"])
    test_dataset = create_dataset(test_config["path"], test_config["type"])
    classifier = create_classifier(classifier_config["type"], config)

    experiment = Experiment(train_dataset, test_dataset)
    metrics = experiment.run(classifier)

    write_report(args[2], config, metrics)

    print("Success.")


if __name__ == "__main__":
    main()
