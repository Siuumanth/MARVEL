import java.util.Scanner;
import java.util.Random;

public class MergeSortExp {
    
    public static void mergeSort(int[] a, int low, int high) {
        int N = high - low;
        if (N <= 1) return;

        int mid = low + (N / 2);

        // Recursively sort both halves
        mergeSort(a, low, mid);
        mergeSort(a, mid, high);

        // Merge the sorted halves
        int[] temp = new int[N];
        int i = low, j = mid;

        for (int k = 0; k < N; k++) {
            if (i == mid) {
                temp[k] = a[j++];
            } else if (j == high || a[i] < a[j]) {
                temp[k] = a[i++];
            } else {
                temp[k] = a[j++];
            }
        }

        // Copy sorted elements back into original array
        for (int k = 0; k < N; k++) {
            a[low++] = temp[k];
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Random r = new Random();

        System.out.println("Merge Sort\nEnter the number of times the algorithm should run:");
        int times = scan.nextInt();
        double totalDuration = 0;

        for (int j = 0; j < times; j++) {
            System.out.println("Random numbers generated at POS " + j + " are:");

            int[] a = new int[10];
            for (int i = 0; i < 10; i++) {
                a[i] = r.nextInt(1000);
                System.out.print(a[i] + " ");
            }

            System.out.println("");

            long startTime = System.nanoTime();
            mergeSort(a, 0, 10);
            long endTime = System.nanoTime();

            double duration = (endTime - startTime);
            System.out.println("Elements after sorting:");
            for (int i = 0; i < 10; i++) {
                System.out.print(a[i] + " ");
            }

            System.out.println("");
            totalDuration += duration;
        }

        System.out.println("\nTotal time taken to sort: " + totalDuration + " Nano Seconds");
        double milliseconds = (totalDuration / 1_000_000);
        System.out.println("Total time taken to sort: " + milliseconds + " Milli Seconds");

        double avgTime = totalDuration / times;
        System.out.println("Average time spent: " + avgTime + " Nano Seconds");

        double avgMilliseconds = avgTime / 1_000_000;
        System.out.println("Average time spent: " + avgMilliseconds + " Milli Seconds");

        scan.close();
    }
}
