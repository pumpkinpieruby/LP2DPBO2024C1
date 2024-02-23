<?php
require("Shirt.php");

$listShirt = array();

$shirt1 = new Shirt("201", "pants", "Zara", "Rp. 299000", "M", "cotton", "Female", "white", "long");
array_push($listShirt, $shirt1);

$shirt2 = new Shirt("202", "cardigan", "Uniqlo", "Rp. 399000", "L", "wool", "Female", "Blue", "long");
array_push($listShirt, $shirt2);
?>
<!DOCTYPE html>
<html>
<head>
    <title>Shirts Table</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }

        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }

        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>

<h2>Shirts Table</h2>

<table>
    <tr>
        <th>ID Product</th>
        <th>Name</th>
        <th>Brand</th>
        <th>Price</th>
        <th>Size</th>
        <th>Material</th>
        <th>Gender</th>
        <th>Color</th>
        <th>Sleeve Type</th>
    </tr>
    <?php foreach ($listShirt as $shirt): ?>
        <tr>
            <td><?php echo $shirt->getIdProduct(); ?></td>
            <td><?php echo $shirt->getName(); ?></td>
            <td><?php echo $shirt->getBrand(); ?></td>
            <td><?php echo $shirt->getPrice(); ?></td>
            <td><?php echo $shirt->getSize(); ?></td>
            <td><?php echo $shirt->getMaterial(); ?></td>
            <td><?php echo $shirt->getGender(); ?></td>
            <td><?php echo $shirt->getColor(); ?></td>
            <td><?php echo $shirt->getSleeveType(); ?></td>
        </tr>
    <?php endforeach; ?>
</table>

</body>
</html>
