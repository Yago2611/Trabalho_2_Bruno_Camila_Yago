
from src.datasets.dataset_factory import create_dataset
from src.classifiers.classifier_factory import create_classifier
from src.experiment import Experiment
from src.io.args import parse_args
from src.io.config import load_config
from src.io.report import write_report


def main():
    args = parse_args()
    config = load_config(args.config_path)

    train_config = config['train_dataset']
    test_config = config['test_dataset']

    train_dataset = create_dataset(train_config["path"], train_config["type"])
    test_dataset = create_dataset(test_config["path"], test_config["type"])
    classifier = create_classifier("knn", config)

    experiment = Experiment(train_dataset, test_dataset)
    metrics = experiment.run(classifier)

    write_report(args.report_path, config, metrics)

    print("Success.")


if __name__ == "__main__":
    main()
