"""I am not sure how to extract the data in the format for e2e from the dataset on Huggingface, so I do it manually
here."""
import json


def construct_sample(paragraph):
    questions = []
    for question in paragraph["qas"]:
        questions.append(question["question"])
    return {"context": paragraph["context"], "questions": questions}


def construct_dataset(data):
    samples = []
    for paragraph_container in data["data"]:
        samples.append(construct_sample(paragraph_container["paragraphs"][0]))
    return {"data": samples}


def prepare_e2e(train_path, test_path):
    with open(train_path, "r") as train_file:
        train_data = json.load(train_file)

    with open("data/e2e_train.json", "w+") as file:
        json.dump(construct_dataset(train_data), file)

    with open(test_path, "r") as test_path:
        test_data = json.load(test_path)

    with open("data/e2e_test.json", "w+") as file:
        json.dump(construct_dataset(test_data), file)


if __name__ == "__main__":
    prepare_e2e("GermanQuAD/GermanQuAD_train.json", "GermanQuAD/GermanQuAD_test.json")
