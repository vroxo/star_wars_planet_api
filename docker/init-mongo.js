db.createUser(
    {
        user: "skywalker",
        pwd: "skywalker",
        roles:
            [
                {
                    role: "readWrite",
                    db: "star_wars_planets"
                }
            ]
    }
)
