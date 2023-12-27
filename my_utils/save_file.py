import csv

def save_to_csv(text):
    csv_file_path = "output.csv"
    data_to_save = [text]
    # CSV 파일에 데이터 쓰기
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        #writer.writerow([today, final_text[1], final_text[2]])
        writer.writerow(['넷플릭스','2023-12-05',text])

    print(f"Data has been saved to {csv_file_path}")