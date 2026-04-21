public class TestQuery {
    public void run(String username, String password) {
        String query = "SELECT * FROM Users WHERE username = '" 
                     + username + "' AND password = '" + password + "'";
        System.out.println(query);
    }
}
