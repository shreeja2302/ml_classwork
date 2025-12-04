
import collect_data as cd


def main():
    # 1) Use CSV data
    csv_df = cd.load_csv()
    print("CSV rows:", len(csv_df))

    # 2) Use JSON data
    json_df = cd.read_json()
    print("JSON users:", list(json_df["user"]))

    # 3) Use logs
    logs_df = cd.read_logs()
    print("Log levels:", logs_df["level"].unique())

    # 4) Use text
    lines = cd.read_text()
    print("First line:", lines[0].strip())

    # 5) Use audio
    audio, sr = cd.read_audio()
    print("Audio length (seconds):", len(audio) / sr)


if __name__ == "__main__":
    main()
