class Review:

    def __init__(self, id, rate, content, fuel_station_id, user_id, created_at, updated_at):
        self.id = id
        self.rate = rate
        self.content = content
        self.fuel_station_id = fuel_station_id
        self.user_id = user_id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f"INSERT INTO Reviews (Id, Rate, Content, UserId, FuelStationId, CreatedAt, CreatedBy, UpdatedAt, UpdatedBy, Deleted) VALUES ({self.id}, {self.rate}, {self.content}, {self.user_id}, {self.fuel_station_id}, '{self.created_at}', {self.user_id}, '{self.updated_at}', {self.user_id}, 0);"