import java.util.*;

class Position {
    int x, y;

    public Position(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public Position copy() {
        return new Position(x, y);
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Position) {
            Position p = (Position) obj;
            return this.x == p.x && this.y == p.y;
        }
        return false;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }

    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}

class Robot {
    private int id;
    private String name;
    private Position position;

    public Robot(int id, String name) {
        this.id = id;
        this.name = name;
        this.position = new Position(0, 0); // Start at top-left
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public Position getPosition() {
        return position;
    }

    public void setPosition(Position newPosition) {
        this.position = newPosition;
    }
}

public class RobotMovementApp {
    private static final int ROWS = 10;
    private static final int COLS = 10;
    private static Map<Integer, Robot> robots = new HashMap<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int robotCounter = 1;

        while (true) {
            System.out.println("\n1. Create Robot");
            System.out.println("2. Move Robot");
            System.out.println("3. Show Robot Location");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");

            int option = sc.nextInt();
            sc.nextLine(); // consume newline

            switch (option) {
                case 1:
                    System.out.print("Enter robot name (e.g., Robot A): ");
                    String robotName = sc.nextLine();
                    Robot robot = new Robot(robotCounter, robotName);
                    robots.put(robotCounter, robot);
                    System.out.println("Robot '" + robotName + "' created with ID: " + robotCounter);
                    robotCounter++;
                    break;

                case 2:
                    System.out.print("Enter Robot ID: ");
                    int id = sc.nextInt();
                    sc.nextLine(); // consume newline
                    if (!robots.containsKey(id)) {
                        System.out.println("Robot not found.");
                        break;
                    }
                    System.out.print("Enter movement (e.g. N4): ");
                    String input = sc.nextLine().toUpperCase();
                    moveRobot(id, input);
                    break;

                case 3:
                    System.out.print("Enter Robot ID: ");
                    int viewId = sc.nextInt();
                    if (!robots.containsKey(viewId)) {
                        System.out.println("Robot not found.");
                    } else {
                        Robot r = robots.get(viewId);
                        System.out.println("Robot " + r.getId() + " (" + r.getName() + ") is at: " + r.getPosition());
                    }
                    break;

                case 4:
                    System.out.println("Exiting program.");
                    sc.close();
                    return;

                default:
                    System.out.println("Invalid option.");
            }
        }
    }

    private static void moveRobot(int id, String command) {
        Robot robot = robots.get(id);
        Position current = robot.getPosition().copy();

        if (command.length() < 2) {
            System.out.println("Invalid command.");
            return;
        }

        char dir = command.charAt(0);
        int steps;
        try {
            steps = Integer.parseInt(command.substring(1));
        } catch (NumberFormatException e) {
            System.out.println("Invalid step count.");
            return;
        }

        for (int i = 0; i < steps; i++) {
            Position next = current.copy();

            switch (dir) {
                case 'N': next.y -= 1; break;
                case 'S': next.y += 1; break;
                case 'E': next.x += 1; break;
                case 'W': next.x -= 1; break;
                default:
                    System.out.println("Invalid direction.");
                    return;
            }

            if (next.x < 0 || next.x >= COLS || next.y < 0 || next.y >= ROWS) {
                System.out.println("Out of bounds. Stopped at " + current);
                break;
            }

            boolean occupied = isOccupied(next, id);
            if (occupied) {
                System.out.println("Position occupied by another robot. Stopped at " + current);
                break;
            }

            current = next;
        }

        robot.setPosition(current);
        System.out.println("Robot " + robot.getId() + " (" + robot.getName() + ") moved to " + current);
    }

    private static boolean isOccupied(Position pos, int currentRobotId) {
        for (Map.Entry<Integer, Robot> entry : robots.entrySet()) {
            if (entry.getKey() != currentRobotId && entry.getValue().getPosition().equals(pos)) {
                return true;
            }
        }
        return false;
    }
}
