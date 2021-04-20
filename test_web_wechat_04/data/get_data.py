import yaml


def get_yaml_data(file):
    with open(file, encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
    return yaml_data


if __name__ == "__main__":
    print(get_yaml_data('./department.yaml'))
