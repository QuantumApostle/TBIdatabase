package dbm;

import java.sql.*;
import java.util.Scanner;

public class MySqlAccess {
	private Connection connect = null;
	private Statement statement = null;
	private PreparedStatement preparedStatement = null;
	private ResultSet resultSet = null;

	// insert new record into database
	public void insertDataBase(Scanner keyboard) throws Exception {
		try {
			Class.forName("com.mysql.jdbc.Driver");
			connect = DriverManager.getConnection("jdbc:mysql://localhost/TBI?"
					+ "user=root&password=eric890125");
			statement = connect.createStatement();
			String table = chooseTable(keyboard);
			String query = null;
			if (table == "exit") {
				close();
				System.exit(0);
			} else {

				int AID;

				switch (table) {

				case "BasicInfo":
					System.out.println("Enter the new animal number");
					AID = keyboard.nextInt();
					System.out
							.println("Enter the new date of birth in format yyyy-mm-dd");
					String DOB = keyboard.next();
					System.out
							.println("Enter the new date of impulse in format yyyy-mm-dd");
					String impulse = keyboard.next();
					query = "insert into TBI." + table
							+ " (AID, DOB, Impulse) values ("
							+ Integer.toString(AID) + ",'" + DOB + "','"
							+ impulse + "');";
					break;

				case "Weight":
					System.out.println("Enter the new animal number");
					AID = keyboard.nextInt();
					System.out
							.println("Enter the new date of weight in format yyyy-mm-dd");
					String weightDate = keyboard.next();
					System.out.println("Enter the new weight");
					Double weight = keyboard.nextDouble();
					query = "insert into TBI." + table
							+ " (AID, WeightDate, Weight) values ("
							+ Integer.toString(AID) + ",'" + weightDate + "',"
							+ Double.toString(weight) + ");";
					break;

				case "GNG":
					System.out.println("Enter the new animal number");
					AID = keyboard.nextInt();
					System.out
							.println("Enter the new date of test in format yyyy-mm-dd");
					String testDate = keyboard.next();
					System.out.println("Enter the correctness");
					Double correctness = keyboard.nextDouble();
					query = "insert into TBI." + table
							+ " (AID, TestDate, Correctness) values ("
							+ Integer.toString(AID) + ",'" + testDate + "',"
							+ Double.toString(correctness) + ");";
					break;
				}
			}

			System.out.println("The query is " + query);
			boolean result = statement.execute(query);
			if (!result) {
				System.out.println("Insert successfully.");
			} else {
				System.out.println("Insert unsuccessfully.");
			}
		} catch (Exception e) {
			throw e;
		} finally {
			close();
		}
	}

	// update database
	public void updateDataBase(Scanner keyboard) throws Exception {
		try {
			Class.forName("com.mysql.jdbc.Driver");
			connect = DriverManager.getConnection("jdbc:mysql://localhost/TBI?"
					+ "user=root&password=eric890125");
			statement = connect.createStatement();
			String table = chooseTable(keyboard);
			String query = null;
			String query1 = null;
			boolean result;
			int choice = 0;

			if (table == "exit") {
				close();
				System.exit(0);
			} else {

				int AID;
				String DOB = null;
				String impulse = null;

				switch (table) {

				case "BasicInfo":
					resultSet = statement
							.executeQuery("select AID from TBI.BasicInfo");
					printAID(resultSet);
					System.out.println("choose the animal number to update");
					AID = keyboard.nextInt();

					System.out.println("Enter 1 to update the date of birth");
					System.out.println("Enter 2 to update the date of impulse");
					System.out.println("Enter 3 to update both");
					choice = keyboard.nextInt();
					switch (choice) {

					case 1:
						System.out
								.println("Enter the new date of birth in format yyyy-mm-dd");
						DOB = keyboard.next();
						query = "update TBI." + table + " set DOB = '" + DOB
								+ "' where AID = " + Integer.toString(AID)
								+ ";";
						break;

					case 2:
						System.out
								.println("Enter the new date of impulse in format yyyy-mm-dd");
						impulse = keyboard.next();
						query += "update TBI." + table + " set Impulse = '"
								+ impulse + "' where AID = "
								+ Integer.toString(AID) + ";";
						break;

					case 3:
						System.out
								.println("Enter the new date of birth in format yyyy-mm-dd");
						DOB = keyboard.next();
						System.out
								.println("Enter the new date of impulse in format yyyy-mm-dd");
						impulse = keyboard.next();
						query = "update TBI." + table + " set DOB = '" + DOB
								+ "' where AID = " + Integer.toString(AID)
								+ ";";
						query1 = "update TBI." + table + " set Impulse = '"
								+ impulse + "' where AID = "
								+ Integer.toString(AID) + ";";
					}

					break;

				case "Weight":
					resultSet = statement
							.executeQuery("select distinct(AID) from TBI.Weight");
					System.out.println("Choose the animal number to update");
					printAID(resultSet);
					AID = keyboard.nextInt();

					resultSet = statement
							.executeQuery("select distinct(WeightDate) from TBI.Weight where AID = "
									+ AID + ";");
					System.out
							.println("Choose the date of weight in format yyyy-mm-dd to update");
					printDate(resultSet, "WeightDate");
					String weightDate = keyboard.next();

					System.out.println("Enter the new weight to update");
					Double weight = keyboard.nextDouble();
					query = "update TBI." + table + " set Weight = "
							+ Double.toString(weight) + " where weightDate = '"
							+ weightDate + "' and " + "AID = "
							+ Integer.toString(AID) + ";";
					break;

				case "GNG":
					resultSet = statement
							.executeQuery("select distinct(AID) from TBI.GNG");
					System.out.println("Choose the animal number to update");
					printAID(resultSet);
					AID = keyboard.nextInt();

					resultSet = statement
							.executeQuery("select distinct(TestDate) from TBI.GNG where AID = "
									+ AID + ";");
					System.out
							.println("Choose the date of test in format yyyy-mm-dd to update");
					printDate(resultSet, "TestDate");
					String testDate = keyboard.next();

					System.out.println("Enter the new correctness to update");
					Double correctness = keyboard.nextDouble();
					query = "update TBI." + table + " set Correctness = "
							+ Double.toString(correctness)
							+ " where TestDate = '" + testDate + "' and "
							+ "AID = " + Integer.toString(AID) + ";";
					break;
				}
			}

			System.out.println("The query is \n" + query);
			statement = connect.createStatement();
			result = statement.execute(query);
			if (!result) {
				System.out.println("Update successfully.");
			} else {
				System.out.println("Update unsuccessfully.");
			}

			if (query1 != null) {
				System.out.println("The query1 is \n" + query1);
				statement = connect.createStatement();
				result = statement.execute(query1);
				if (!result) {
					System.out.println("Update successfully.");
				} else {
					System.out.println("Update unsuccessfully.");
				}
			}
		} catch (Exception e) {
			throw e;
		} finally {
			close();
		}
	}

	// show average weights for each animal
	public void avgWeights() throws Exception {
		try {
			Class.forName("com.mysql.jdbc.Driver");
			connect = DriverManager.getConnection("jdbc:mysql://localhost/TBI?"
					+ "user=root&password=eric890125");
			statement = connect.createStatement();
			String query = "select AID, avg(weight) as AverageWeight from TBI.Weight group by AID;";
			statement = connect.createStatement();
			resultSet = statement.executeQuery(query);
			System.out.println("AID\t Average Weights");
			while (resultSet.next()) {
				String AID = resultSet.getString("AID");
				String avgWeight = resultSet.getString("AverageWeight");
				System.out.println(AID + "\t" + avgWeight);
			}

		} catch (Exception e) {
			throw e;
		} finally {
			close();
		}
	}

	// show maximal correctness for chosen animal
	public void maxCorrectness(Scanner keyboard) throws Exception {
		try {
			Class.forName("com.mysql.jdbc.Driver");
			connect = DriverManager.getConnection("jdbc:mysql://localhost/TBI?"
					+ "user=root&password=eric890125");
			statement = connect.createStatement();

			resultSet = statement
					.executeQuery("select distinct(AID) from TBI.GNG");
			System.out.println("Choose the animal number:");
			printAID(resultSet);
			String AID = keyboard.next();

			String query = "select TestDate, max(Correctness) as Max_Correctness from TBI.GNG where AID = "
					+ AID;
			resultSet = statement.executeQuery(query);

			while (resultSet.next()) {
				String maxCt = resultSet.getString("Max_Correctness");
				String testDate = resultSet.getString("TestDate");
				System.out.println("For " + AID
						+ ", the maximal correctness is " + maxCt + " at "
						+ testDate + ".");
			}

		} catch (Exception e) {
			throw e;
		} finally {
			close();
		}
	}

	// delete record in table balance beam with too long time duration
	public void deleteLongDuration(Scanner keyboard) throws Exception {
		try {
			Class.forName("com.mysql.jdbc.Driver");
			connect = DriverManager.getConnection("jdbc:mysql://localhost/TBI?"
					+ "user=root&password=eric890125");
			statement = connect.createStatement();

			System.out.println("Enter the time limit in second:");
			String timeLimit = keyboard.next();

			String query = "delete from TBI.BalanceBeam where duration > "
					+ timeLimit;
			Boolean result = statement.execute(query);
			if (!result) {
				System.out.println("Delete successfully.");
			} else {
				System.out.println("Delete unsuccessfully.");
			}

		} catch (Exception e) {
			throw e;
		} finally {
			close();
		}
	}

	// choose table
	private String chooseTable(Scanner keyboard) {
		String table = null;
		boolean flag = true;
		System.out.println("Enter 1 to choose table Basic Information.");
		System.out.println("Enter 2 to choose table Weight.");
		System.out.println("Enter 3 to choose table Go/No Go experiment.");
		int choice = keyboard.nextInt();
		while (flag) {

			switch (choice) {
			case 1:
				System.out.println("You choose table Basic Infomation");
				table = "BasicInfo";
				flag = false;
				break;
			case 2:
				System.out.println("You choose table Weight.");
				table = "Weight";
				flag = false;
				break;
			case 3:
				System.out.println("You choose table Go/No Go experiment.");
				table = "GNG";
				flag = false;
				break;

			default:
				System.out.println("Invalid input. Please choose again.");
				choice = keyboard.nextInt();
				break;
			}

		}
		return table;
	}

	// print available dates
	private void printDate(ResultSet resultSet, String dateType)
			throws SQLException {
		System.out.println("Available dates are:\n ");
		while (resultSet.next()) {

			String date = resultSet.getString(dateType);
			System.out.println(date);
		}

	}

	// print available animal ids
	private void printAID(ResultSet resultSet) throws SQLException {
		System.out.println("Available Animal IDs are:\n ");
		while (resultSet.next()) {

			String AID = resultSet.getString("AID");
			System.out.print(AID + " ");

		}
		System.out.println();

	}

	// close all connections
	private void close() {
		try {
			if (resultSet != null) {
				resultSet.close();
			}

			if (statement != null) {
				statement.close();
			}

			if (connect != null) {
				connect.close();
			}

			if (preparedStatement != null) {
				preparedStatement.close();
			}
		} catch (Exception e) {

		}
	}

}
