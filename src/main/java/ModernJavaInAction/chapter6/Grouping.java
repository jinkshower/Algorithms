package ModernJavaInAction.chapter6;

import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.Set;
import java.util.stream.Collectors;

public class Grouping {

    enum CaloricLevel {DIET, NORMAL, FAT}

    ;

    public static void main(String[] args) {
        System.out.println("Dishes grouped by type: " + groupDishesByType());
        System.out.println("Dishes grouped by caloric level: " + groupDishesByCaloricLevel());
        System.out.println("Caloric dishes grouped by type: " + groupCaloricDishesByType());
        System.out.println("Dish names grouped by type: " + groupDishNamesByType());
        System.out.println("Dish tags grouped by type: " + groupDishTagsByType());
        System.out.println("max dish" + groupDishMyri());
    }

    private static Map<Dish.Type, List<Dish>> groupDishesByType() {
        return Dish.menu.stream().collect(Collectors.groupingBy(Dish::getType));
    }

    private static Map<CaloricLevel, List<Dish>> groupDishesByCaloricLevel() {
        return Dish.menu.stream().collect(Collectors.groupingBy(
                dish -> {
                    if (dish.getCalories() <= 400) {
                        return CaloricLevel.DIET;
                    } else if (dish.getCalories() <= 700) {
                        return CaloricLevel.NORMAL;
                    } else {
                        return CaloricLevel.FAT;
                    }
                }
        ));
    }

    private static Map<Dish.Type, List<Dish>> groupCaloricDishesByType() {
        return Dish.menu.stream().collect(
                Collectors.groupingBy(Dish::getType,
                        Collectors.filtering(dish -> dish.getCalories() > 500, Collectors.toList())));
    }

    private static Map<Dish.Type, List<String>> groupDishNamesByType() {
        return Dish.menu.stream().collect(
                Collectors.groupingBy(Dish::getType,
                        Collectors.mapping(Dish::getName, Collectors.toList()))
        );
    }

    private static Map<Dish.Type, Set<String>> groupDishTagsByType() {
        return Dish.menu.stream().collect(
                Collectors.groupingBy(Dish::getType,
                        Collectors.flatMapping(dish -> Dish.dishTags.get(dish.getName()).stream(), Collectors.toSet()))
        );
    }

    private static Map<Dish.Type, Optional<Dish>> groupDishMyri() {
        return Dish.menu.stream().collect(
                Collectors.groupingBy(Dish::getType, Collectors.maxBy(Comparator.comparing(Dish::getCalories)))
        );
    }
}
