CREATE TABLE leaderboard_history (
    id INT AUTO_INCREMENT,
    uid INT NOT NULL,
    mode TINYINT(2) NOT NULL,
    player_rank INT(7) NOT NULL,
    capture_time INT(11) NOT NULL,
    PRIMARY KEY (id)
);
