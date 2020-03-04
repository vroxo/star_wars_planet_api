db.createUser(
    {
        user: "skywalker",
        pwd: "skywalker",
        roles:
            [
                {
                    role: "readWrite",
                    db: "star_wars_planets"
                },
                {
                    role: "readWrite",
                    db: "star_wars_planets_test"
                }
            ]
    }
)
