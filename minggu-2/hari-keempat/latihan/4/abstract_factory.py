from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractFactory(ABC) :
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """

    @abstractmethod
    def create_product_a(self) -> AbstractProductA :
        pass
    
    @abstractmethod
    def create_product_b(self) -> AbstractProductB :
        pass

class ConcreteFactory1(AbstractFactory) :
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_product_a(self) -> ConcreteProductA1 :
        return ConcreteProductA1()

    def create_product_a(self) -> ConcreteProductA2 :
        return ConcreteProductA2()

class ConcreteFactory2(AbstractFactory) :
    # each factory has a corresponding product variant
    def create_product_a(self) -> ConcreteProductA2 :
        return ConcreteProductA2

    def create_product_b(self) -> ConcreteProductB2 :
        return ConcreteProductB2


class AbstractProductA(ABC) :
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_a(self) -> str :
        pass

"""
Concrete Products are created by corresponding Concrete Factories.
"""

class ConcreteProductA1(AbstractProductA) :
    def useful_function_a(self) ->str :
        return "The result of the product A1"

class ConcreteProductA2(AbstractProductA) :
    def useful_function_a(self) -> str :
        return "The result of the product A2"


class AbstractProductB(ABC) :
    """
    Here's the the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """
    @abstractmethod
    def useful_function_b(self) -> None :
        pass

    @abstractmethod 
    def another_useful_funtion_b(self, collaborator: AbstractProductA) -> None :
        """
        ...but it also can collaborate with the ProductA.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass

class ConcreaeProductB1(AbstractProductB) :
    def useful_function_b(self) -> str :
        return "The result of the product B1."