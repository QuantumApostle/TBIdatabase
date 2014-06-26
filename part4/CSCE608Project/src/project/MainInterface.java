/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package project;

import java.util.Scanner;

/**
 *
 * @author YixinGeng
 */
public class MainInterface {

    public static void main(String[] args) throws Exception {
        MySqlAccess db = new MySqlAccess();
        boolean flag = true;

        System.out.println("This is the management system for database TBI.");
        System.out.println("Enter 1 to insert new data.");
        System.out.println("Enter 2 to update data.");
        System.out.println("Enter 3 to show average weights for each animals.");
        System.out.println("Enter 4 to show maximal correctness and test date in Go/No Go experiment.");
        System.out.println("Enter 5 to delete record with too long duration in BalanceBeam experiment.");
        System.out.println("Enter 0 to exit.");

        Scanner keyboard = new Scanner(System.in);
        int choice = keyboard.nextInt();

        while (flag) {

            switch (choice) {
                case 1:
                    System.out.println("You choose to insert new data.");
                    db.insertDataBase(keyboard);
                    flag = false;
                    break;

                case 2:
                    System.out.println("You choose to update data.");
                    db.updateDataBase(keyboard);
                    flag = false;
                    break;

                case 3:
                    System.out.println("You choose to show average weights for each animals.");
                    db.avgWeights();
                    flag = false;
                    break;

                case 4:
                    System.out.println("You choose to show maximal correctness and test date in experiment Go/No Go.");
                    db.maxCorrectness(keyboard);
                    flag = false;
                    break;

                case 5:
                    System.out.println("You choose to delete record with too long duration in BalanceBeam experiment.");
                    db.deleteLongDuration(keyboard);
                    flag = false;
                    break;

                case 0:
                    System.out.println("You choose to exit.");
                    flag = false;
                    break;

                default:
                    System.out.println("Invalid input. Please choose again.");
                    choice = keyboard.nextInt();
                    break;
            }

        }

        keyboard.close();
    }
}
