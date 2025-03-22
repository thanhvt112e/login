import os
import json


class DataConnector:
    def __init__(self):
        """Khởi tạo đường dẫn và đảm bảo file players.json tồn tại."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.folder_path = os.path.join(base_dir, "..", "dataset")
        self.filename = os.path.join(self.folder_path, "players.json")
        self.ensure_file_exists()

    def signup(self, username, password):
        players = self.get_all_players()
        new_player = {"username": username, "password": password}
        players.append(new_player)
        try:
            with open(self.filename, "w") as f:
                json.dump(players, f, indent=4)
            return True
        except Exception:
            return False

    def ensure_file_exists(self):
        """Tạo thư mục dataset và file players.json nếu chưa tồn tại."""
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)  # Tạo thư mục nếu chưa có

        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)  # Tạo file JSON rỗng

    def load_users(self):
        """Đọc danh sách người dùng từ file JSON."""
        with open(self.filename, "r") as f:
            return json.load(f)

    def save_users(self, users):
        """Ghi danh sách người dùng vào file JSON."""
        with open(self.filename, "w") as f:
            json.dump(users, f, indent=4)

    def add_user(self, username, password):
        """Thêm người dùng mới vào danh sách."""
        users = self.load_users()
        users.append({"username": username, "password": password})
        self.save_users(users)

    def validate_user(self, username, password):
        """Kiểm tra thông tin đăng nhập."""
        users = self.load_users()
        for user in users:
            if user["username"] == username and user["password"] == password:
                return True
        return False

    def get_all_players(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except Exception:
            return []

    def login(self, username, password):
        players = self.get_all_players()
        for player in players:
            if player["username"] == username and player["password"] == password:
                return player
        return None


